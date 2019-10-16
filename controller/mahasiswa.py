from flask import Blueprint, redirect,render_template, request, flash
from config.db import mysql
import pymysql

mahasiswa = Blueprint('mahasiswa',__name__)


@mahasiswa.route('/')
def list_mahasiswa():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql_mahasiswa = "SELECT * FROM t_mahasiswa"
    cursor.execute(sql_mahasiswa)
    mahasiswa = cursor.fetchall()
    return render_template('listmahasiswa.html', mahasiswa=mahasiswa)


@mahasiswa.route('/add-mahasiswa')
def add_mahasiswa():
    return render_template('addmahasiswa.html')


@mahasiswa.route('/save-mahasiswa', methods=['POST'])
def save_mahasiswa():
    nim = request.form['nim']
    nama_lengkap = request.form['nama_lengkap']
    email = request.form['email']
    tanggal_lahir = request.form['tanggal_lahir']
    jurusan = request.form['jurusan']
    alamat = request.form['alamat']
    if nim and nama_lengkap and email and tanggal_lahir and jurusan and alamat and request.method == 'POST':
        sql = "INSERT INTO t_mahasiswa(nim, nama_lengkap, email, tanggal_lahir, jurusan, alamat) VALUES(%s, %s, %s, %s, %s, %s)"
        data = (nim, nama_lengkap, email, tanggal_lahir, jurusan, alamat)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        flash('Save Successfully !')
        return redirect('/')
    else:
        flash('Save Failed !')
        return redirect('/add-mahasiswa')


@mahasiswa.route('/edit-mahasiswa/<int:id>')
def edit_mahasiswa(id):
    sql = "SELECT * FROM t_mahasiswa WHERE id=%s"
    id = id
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql,id)
    mahasiswa = cursor.fetchone()
    return render_template('editmahasiswa.html', mahasiswa=mahasiswa)


@mahasiswa.route('/update-mahasiswa', methods=['POST'])
def update_mahasiswa():
    id = request.form['id']
    nim = request.form['nim']
    nama_lengkap = request.form['nama_lengkap']
    email = request.form['email']
    tanggal_lahir = request.form['tanggal_lahir']
    jurusan = request.form['jurusan']
    alamat = request.form['alamat']
    if id and nim and nama_lengkap and email and tanggal_lahir and jurusan and alamat and request.method == 'POST':
        sql = "UPDATE t_mahasiswa SET nim=%s, nama_lengkap=%s, email=%s, tanggal_lahir=%s, jurusan=%s, alamat=%s WHERE id=%s"
        data = (nim, nama_lengkap, email, tanggal_lahir, jurusan, alamat, id)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        flash('Update Successfully !')
        return redirect('/')
    else:
        flash('Update Failed !')
        return redirect('/edit-mahasiswa')


@mahasiswa.route('/delete-mahasiswa/<int:id>')
def delete_mahasiswa(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "DELETE FROM t_mahasiswa WHERE id=%s"
    cursor.execute(sql, id)
    conn.commit()
    flash('Deleted successfully !')
    return redirect('/')