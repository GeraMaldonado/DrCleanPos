from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDFlatButton
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from datetime import datetime, date
from database import bd,clientes,notas,lista_precios
from kivy.metrics import dp
import pandas as pd
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCardSwipe, MDCard, MDSeparator
from kivy.animation import Animation
from kivymd.uix.list import MDList
from kivy.properties import StringProperty,BooleanProperty,NumericProperty,ObjectProperty
import os
import requests
import matplotlib
from kivymd.utils import asynckivy as ak
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.clipboard import Clipboard
from kivy.config import Config
from kivy_garden.mapview import MapMarkerPopup
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


def get_app():
    return MDApp.get_running_app()