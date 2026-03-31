from django.shortcuts import render

def public_home(request):
    members = [
        {
            'name': 'Samuel Indriano',
            'npm': '2406400524',
            'role': 'Integrator & Base Setup',
            'bio': 'Bertanggung jawab atas base project, integrasi final, merapikan routing dan base template, serta membereskan conflict dan testing flow akhir.',
        },
        {
            'name': 'Aaron Nathanael Suhaendi ',
            'npm': '2406437073',
            'role': 'Halaman Biodata Publik',
            'bio': 'Bertanggung jawab atas pembuatan homepage publik, card anggota kelompok, deskripsi kelompok, dan tampilan biodata yang rapi tanpa perlu login.',
        },
        {
            'name': 'Wildan Anshari Hidayat',
            'npm': '2406396590',
            'role': 'Authentication Google OAuth',
            'bio': 'Bertanggung jawab atas fitur login dan logout Google OAuth, redirect, dan mengatur kondisi user yang sudah login vs belum login.',
        },
        {
            'name': 'Ahmad Anggara Bayuadji Prawirosoenoto',
            'npm': '2406495514',
            'role': 'Authorization',
            'bio': 'Bertanggung jawab atas otorisasi, whitelist email anggota, membedakan editor dan viewer, serta memproteksi halaman edit dari akun luar.',
        },
        {
            'name': 'Muhammad Rizky Antariksa',
            'npm': '2406495552',
            'role': 'Fitur Ubah Tampilan',
            'bio': 'Bertanggung jawab atas halaman settings/theme, fitur ubah warna dan font, menyimpan perubahan, serta menampilkannya di website.',
        }
    ]
    
    context = {
        'members': members,
    }
    return render(request, 'main/public_home.html', context)
