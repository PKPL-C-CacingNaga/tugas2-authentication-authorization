from django.shortcuts import render

def public_home(request):
    members = [
        {
            'name': 'Samuel Indriano',
            'npm': '2406400524',
            'prodi': 'Ilmu Komputer',
            'role': 'Project Integration & Base Setup',
            'bio': 'Bertanggung jawab atas penyusunan base project, integrasi awal, perapihan routing dan base template, serta pengujian alur utama aplikasi.',
            'photo': 'main/images/samuel-indriano.jpeg',
        },
        {
            'name': 'Aaron Nathanael Suhaendi ',
            'npm': '2406437073',
            'prodi': 'Ilmu Komputer',
            'role': 'Public Profile Experience',
            'bio': 'Bertanggung jawab atas pembuatan homepage publik, card anggota kelompok, deskripsi kelompok, dan tampilan biodata yang rapi tanpa perlu login.',
            'photo': 'main/images/aaron-nathanael-suhaendi.jpeg',
        },
        {
            'name': 'Wildan Anshari Hidayat',
            'npm': '2406396590',
            'prodi': 'Ilmu Komputer',
            'role': 'Google OAuth Authentication',
            'bio': 'Bertanggung jawab atas fitur login dan logout Google OAuth, redirect, dan mengatur kondisi user yang sudah login vs belum login.',
            'photo': 'main/images/wildan-anshari-hidayat.jpeg',
            'photo_class': 'member-photo-wildan',
        },
        {
            'name': 'Ahmad Anggara Bayuadji Prawirosoenoto',
            'npm': '2406495514',
            'prodi': 'Ilmu Komputer',
            'role': 'Access Control & Authorization',
            'bio': 'Bertanggung jawab atas otorisasi, whitelist email anggota, membedakan editor dan viewer, serta memproteksi halaman edit dari akun luar.',
            'photo': 'main/images/ahmad-anggara-bayuadji.jpeg',
        },
        {
            'name': 'Muhammad Rizky Antariksa',
            'npm': '2406495552',
            'prodi': "Ilmu Komputer",
            'role': 'Theme Customization',
            'bio': 'Bertanggung jawab atas halaman settings/theme, fitur ubah warna dan font, menyimpan perubahan, serta menampilkannya di website.',
            'photo': 'main/images/muhammad-rizky-antariksa.jpeg',
        }
    ]

    context = {
        'members': members,
    }
    return render(request, 'main/public_home.html', context)
