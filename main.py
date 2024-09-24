import flet as ft
import mysql.connector
from openpyxl import Workbook

# Koneksi ke database MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mobile_app"
)

cursor = mydb.cursor()

def main(page: ft.Page):
    page.title = "User Subscription Table"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 475
    page.window_width = 830
    page.window_maximizable = False

    # Definisikan DataTable
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("Age")),
            ft.DataColumn(ft.Text("Subscription")),
            ft.DataColumn(ft.Text("Employment")),
        ],
        rows=[],  # Inisialisasi rows kosong
    )

    # Fungsi untuk mengambil data dari database dan mengisi DataTable
    def tampil_user():
        sql = "SELECT * FROM user_subs"
        cursor.execute(sql)
        result = cursor.fetchall()

        # Loop data dari database dan tambahkan ke DataTable
        for row in result:
            data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row[1])),  # Name
                        ft.DataCell(ft.Text(str(row[2]))),  # Age
                        ft.DataCell(ft.Text(row[3])),  # Subscription
                        ft.DataCell(ft.Text(row[4])),  # Employment
                    ]
                )
            )
        page.update()

    # Buat form input untuk menambah data baru
    name_input = ft.TextField(label="Name")
    age_input = ft.TextField(label="Age")  # Gunakan TextField untuk Age
    subscription_input = ft.Dropdown(
        label="Subscription",
        options=[
            ft.dropdown.Option("Subscribed"),
            ft.dropdown.Option("Not Subscribed"),
            ft.dropdown.Option("Other"),
        ],
    )
    employed_input = ft.Checkbox(label="Employed")

    # Aksi ketika menekan tombol Insert untuk menambah row baru
    def add_row(e):
        # Pastikan nilai Age adalah angka
        if age_input.value.isdigit():
            new_row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(name_input.value)),
                    ft.DataCell(ft.Text(age_input.value)),
                    ft.DataCell(ft.Text(subscription_input.value)),
                    ft.DataCell(ft.Text("Employed" if employed_input.value else "Unemployed")),
                ]
            )
            data_table.rows.append(new_row)
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Age must be a number!"))
            page.snack_bar.open = True
            page.update()

    # Fungsi untuk menyimpan data ke database
    def insert_data(e):
        if age_input.value.isdigit():
            employment_status = "Employed" if employed_input.value else "Unemployed"
            insert_query = "INSERT INTO user_subs (name, age, subscription, employment) VALUES (%s, %s, %s, %s)"
            values = (name_input.value, age_input.value, subscription_input.value, employment_status)
            cursor.execute(insert_query, values)
            mydb.commit()

            # Setelah insert, tambah row baru ke DataTable
            add_row(e)

            # Bersihkan input setelah data di-insert
            name_input.value = ""
            age_input.value = ""
            subscription_input.value = None
            employed_input.value = False
            page.update()

        else:
            page.snack_bar = ft.SnackBar(ft.Text("Age must be a number!"))
            page.snack_bar.open = True
            page.update()

    # Layout
    page.add(
        ft.Row([
            ft.Container(
                ft.Column([
                    ft.Text("Insert Row", size=18, weight="bold"),
                    name_input,
                    age_input,
                    subscription_input,
                    employed_input,
                    ft.ElevatedButton("Insert", on_click=insert_data, color=ft.colors.BLUE),
                    ft.Switch(label="Mode", value=True),
                ], expand=1),
                border=ft.border.all(1, ft.colors.GREY),  # Tambahkan border abu-abu
                padding=10,
                height=400,
            ),
            ft.Container(
                ft.Column([
                    ft.VerticalDivider(),
                    data_table,
                ]),
                border=ft.border.all(1, ft.colors.GREY),  # Tambahkan border abu-abu
                padding=10,
                height=400,
            )
        ])
    )

    # Panggil fungsi untuk menampilkan data dari database
    tampil_user()

# Jalankan aplikasi
ft.app(target=main)
