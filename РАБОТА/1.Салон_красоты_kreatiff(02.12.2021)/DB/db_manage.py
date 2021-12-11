import sqlite3 as sq
from loader import bot, dp
from aiogram import types

with sq.connect('DB\database.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOt EXISTS price_man (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_ped (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_m (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')

    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_cut (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_laying (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_care (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_bar_coloring (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')

    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_brow (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_lash (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_ear (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_epil (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_depil (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOt EXISTS price_cos_face (name TEXT, price TEXT, sms_1 TEXT, sms_2 TEXT)')


async def show_price_man():
    return cur.execute('SELECT name, price FROM price_man').fetchall()

async def show_price_ped():
    return cur.execute('SELECT name, price FROM price_ped').fetchall()

async def show_price_bar_m():
    return cur.execute('SELECT name, price FROM price_bar_m').fetchall()

async def show_price_cut():
    return cur.execute('SELECT name, price FROM price_bar_cut').fetchall()

async def show_price_coloring():
    return cur.execute('SELECT name, price FROM price_bar_coloring').fetchall()

async def show_price_laying():
    return cur.execute('SELECT name, price FROM price_bar_laying').fetchall()

async def show_price_care():
    return cur.execute('SELECT name, price FROM price_bar_care').fetchall()

async def show_price_lash():
    return cur.execute('SELECT name, price FROM price_cos_lash').fetchall()

async def show_price_face():
    return cur.execute('SELECT name, price FROM price_cos_face').fetchall()

async def show_price_epil():
    return cur.execute('SELECT name, price FROM price_cos_epil').fetchall()

async def show_price_depil():
    return cur.execute('SELECT name, price FROM price_cos_depil').fetchall()

async def show_price_brow():
    return cur.execute('SELECT name, price FROM price_cos_brow').fetchall()

async def show_price_ear():
    return cur.execute('SELECT name, price FROM price_cos_ear').fetchall()

