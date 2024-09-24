#memasukkan library flet ke aplikasi
#import flet as ft
import flet
from flet import *
from openpyxl import *

#buat class untuk form/halaman

#function/fungsi utama
def main (page : Page):
    #mengatur halaman
    page.title = "Aplikasi Flet"
    page.window_width = 1280
    page.window_height = 720
    page.window_resizable = False
    page.window_maximizable = True
    page.window_minimizable = True
    page.scroll = "adaptive"
    page.theme_mode = ThemeMode.DARK

    #buat variabel inputan
    inputan_id_dosen = TextField(visible = False, expand = True)
    inputan_nidn_dosen = TextField(label = "NIDN Dosen", hint_text = "masukkan NIDN dosen ... ", expand = True)
    inputan_nama_dosen = TextField(label = "Nama Dosen", hint_text = "masukkan nama dosen ... ", expand = True)
    inputan_jk_dosen = Dropdown(label = "Jenis Kelamin", hint_text = "pilih jenis kelamin dosen ... ", expand = True,
            options=[
                dropdown.Option("Laki-laki"),
                dropdown.Option("Perempuan"),
            ],
        )
    inputan_tgl_lahir_dosen = TextField(label = "Tanggal Lahir", hint_text = "masukkan tgl. lahir dosen ... ", expand = True, read_only = True)
        
    inputan_alamat_dosen = TextField(
            label = "Alamat",
            hint_text = "masukkan alamat kamu ... ",
            expand = True,
            multiline = True,
            max_lines = 3,
            min_lines = 2
        )
    
    page.add(
        Row(
            [
                Container(
                    Column(
                        controls = [
                            Text("Form Entri Dosen", weight = FontWeight.BOLD, size = 20),
                            inputan_id_dosen,
                            inputan_nidn_dosen,
                            inputan_nama_dosen,
                            inputan_jk_dosen,
                            inputan_tgl_lahir_dosen,
                            inputan_alamat_dosen,
                            ElevatedButton(
                                    "Simpan Data",
                                        icon = "SAVE_AS",
                                        icon_color = "white",
                                        color = "white",
                                        bgcolor = "teal",
                                        width = 280,
                                        height = 50,
                                    )
                            
                        ],
                        horizontal_alignment = CrossAxisAlignment.CENTER,
                        #tight = True,
                    ),
                    padding = 25,
                    width = 380,
                    height = 450,
                    border = border.all(1, colors.BLACK),
                    border_radius = border_radius.all(5)
                ),

                Container(
                    Column(
                        [
                            Text("Tabel Data Dosen", weight = FontWeight.BOLD, size = 20),
                            DataTable(
                                columns=[
                                    DataColumn(Text("No")),
                                    DataColumn(Text("NIDN"), numeric=True),
                                    DataColumn(Text("Nama Dosen")),
                                    DataColumn(Text("Jenis Kelamin")),
                                    DataColumn(Text("Umur"), numeric=True),
                                    DataColumn(Text("Alamat")),
                                ],
                                rows=[
                                    DataRow(
                                        cells=[
                                            DataCell(Text("1")),
                                            DataCell(Text("30031830180")),
                                            DataCell(Text("John Doe")),
                                            DataCell(Text("Laki-laki")),
                                            DataCell(Text("29")),
                                            DataCell(Text("Kudus")),
                                        ],
                                    ),
                                    DataRow(
                                        cells=[
                                            DataCell(Text("2")),
                                            DataCell(Text("30031830199")),
                                            DataCell(Text("Ahmad Kuirniawan")),
                                            DataCell(Text("Laki-laki")),
                                            DataCell(Text("25")),
                                            DataCell(Text("Kudus")),
                                        ],
                                    ),
                                    DataRow(
                                        cells=[
                                            DataCell(Text("3")),
                                            DataCell(Text("30031830181")),
                                            DataCell(Text("Delvina Putri")),
                                            DataCell(Text("Perempuan")),
                                            DataCell(Text("27")),
                                            DataCell(Text("Kudus")),
                                        ],
                                    ),
                                    
                                ],
                            ),
                        ]
                    ),
                    padding = 25,
                    width = 850,
                    height = 450,
                    border = border.all(1, colors.BLACK),
                    border_radius = border_radius.all(5)
                )
            ]
        )
                            
    )


#mengatur output aplikasi
flet.app(target = main)
