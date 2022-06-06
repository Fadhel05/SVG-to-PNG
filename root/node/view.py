
import cairosvg
from PIL import Image, ImageDraw, BmpImagePlugin, ImageFile,ImageTransform,Image
# BmpImagePlugin.BmpRleDecoder
# BmpImagePlugin.Image.open()
from PIL.PngImagePlugin import PngImageFile
from django.http import HttpResponse
from pylunasvg import Document, Bitmap
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import os
from wand import image as imim
import cairo
# misc.
from svglib import svglib
import subprocess
import io
import pyinkscape

from root.node import rsvg
from root.node.models import Mode
import numpy as np
import json
import base64
from urllib import request as rr
class Convert(APIView):
    """

    saya membuat fungsi ini agar supaya gambar yang diconvert diperlu di simpan dalam program, akan tetapi ada 1 gambar yang saya coba
    convert akan tetapi tidak bisa diconvert dengan sempurna dan program bisa saja langsung berhenti, saya tidak tahu dimana kesalahannya
    soalnya error tidak terlihat akan tetapi terakhir saya coba, semua gambar bisa terdownload dan program tidak berhenti secara tiba tiba,
    insha allah dapat berfungsi dengan baik.

    """
    def post(self,request,format=None):
        # idx = Mode.objects.create(**{"text":"a"})
        rrr = True
        try:
            # x = request.FILES["foto"]
            # ddd = Document.loadFromData(x.read())
            # ddd = ddd.renderToBitmap(width=int(request.data["width"]),height=int(request.data["height"]))
            # yyy = np.asarray(ddd)
            # imge = Image.fromarray(yyy)
            # imge = imge.resize((int(request.data["width"]),int(request.data["height"])))
            # bytess = io.BytesIO()
            # imge.save(bytess,'PNG')
            x = request.FILES["foto"]
            p = cairosvg.svg2svg(file_obj=x)
            ddd = Document.loadFromData(p)
            # print(ddd.valid())
            ddd = ddd.renderToBitmap(width=int(request.data["width"]),height=int(request.data["height"]))
            yyy = np.asarray(ddd)
            imge = Image.fromarray(yyy)
            imge.resize((int(request.data["width"]), int(request.data["height"])))
            bytess = io.BytesIO()
            imge.save(bytess, "PNG")
        except Exception as e:
            print(str(e))
            rrr = False
            pass
        if rrr:
            return HttpResponse(bytess.getvalue(),content_type="image/png")
        return Response(status=status.HTTP_400_BAD_REQUEST)
class Convert3(APIView):
    def post(self,request,format=None):
        """fungsi ini dapat menconvert gambar dengan baik dan tidak perlu tersimpan, hanya mengandalkan convert data type, akan
           tetapi hasilnya menjadi sedikit aneh jika saya menghapus baris "if request.data["width"] != request.data["height"]:",
           oleh karena itu widht dan height yang diinput harus tetapi sama"""
        rrr = True
        if request.data["width"] != request.data["height"]:
            return Response({"Message":"tidak sama"},status=status.HTTP_400_BAD_REQUEST)
        x = request.FILES["foto"]
        bytess = io.BytesIO()
        try:
            cairosvgfile = cairosvg.svg2png(file_obj=x,write_to=bytess,output_width=int(request.data["width"]),output_height=int(request.data["height"]))
        except Exception as e:
            print(str(e))
            rrr = False
            pass
        if rrr:
            return HttpResponse(bytess.getvalue(),content_type="image/png")
        return Response(status=status.HTTP_400_BAD_REQUEST)
class Convert4(APIView):
    def post(self,request,format=None):
        """saya mencoba membuat fungsi ini menggunakan rsvg wrapper, akan tetapi sangat rumit sehingga saya harus mengintall
        GTK3 runtime, dan menambah code "os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")" pada file rsvg, akan
        tetapi tidak bisa karena overflow int too long to convert """
        rrr = True
        x = request.FILES["foto"]
        bytess = io.BytesIO()
        try:
            cairosvgfile = cairosvg.svg2svg(file_obj=x)
            p = rsvg.rsvgClass()
            h = p.Handle(cairosvgfile)
            print("heheway")
            s = cairo.ImageSurface(cairo.FORMAT_ARGB32,int(request.data["width"]),int(request.data["height"]))
            print("hehway")
            ctx = cairo.Context(s)
            print("hehwway")
            h.render_cairo(ctx)
            print("done")
        except Exception as e:
            print(str(e))
            rrr = False
            pass
        if rrr:
            return HttpResponse(bytess.getvalue(),content_type="image/png")
        return Response(status=status.HTTP_400_BAD_REQUEST)
class Convert5(APIView):
    def post(self,request,format=None):
        """fungsi dapat berfungsi dengan baik, sangat cepat dan terconvert dengan sempurna, tidak masalah jika widht
           dan height di input berbeda karena library akan menyesuaikan dan outputnya width dan heightnya sama panjang"""
        rrr = True
        x = request.FILES["foto"]
        bytess = io.BytesIO()
        try:
            cairosvgfile = cairosvg.svg2svg(file_obj=x)
            t = imim.Image( blob=x,height=int(request.data["height"]), width=int(request.data["width"]))
            # t = imim.Image( blob=cairosvgfile,height=int(request.data["height"]), width=int(request.data["width"]))
            t = t.convert("PNG")
            t.save(bytess)
        except Exception as e:
            print(str(e))
            rrr = False
            pass
        if rrr:
            return HttpResponse(bytess.getvalue(),content_type="image/png")
        return Response(status=status.HTTP_400_BAD_REQUEST)
class Convert6(APIView):
    """fungsi dapat berfungsi dengan baik, sangat cepat dan terconvert dengan sempurna, tidak masalah jika widht
       dan height di input berbeda, panjang width dan height tidak selalu sama karena output dari widht dan height
       berdasarkan input"""
    def post(self,request,format=None):
        rrr = True
        x = request.FILES["foto"]
        bytess = io.BytesIO()
        butes = io.BytesIO()
        try:
            cairosvgfile = cairosvg.svg2svg(file_obj=x)
            t = imim.Image(blob=x, height=int(request.data["height"]), width=int(request.data["width"]))
            t = t.convert("PNG")
            t.save(bytess)
            imge = Image.open(bytess)
            imge = imge.resize((int(request.data["height"]),int(request.data["width"])))
            imge.save(butes,"PNG")
        except Exception as e:
            print(str(e))
            rrr = False
            pass
        if rrr:
            return HttpResponse(butes.getvalue(),content_type="image/png")
        return Response(status=status.HTTP_400_BAD_REQUEST)
class Convert2(APIView):
    """

    sebelum Convert saya membuat Convert 2 pertama kali, fungsi ini berjalan dengan baik, semua bisa ter convert dengan sempurna
    kekurangannya adalah banyak proses yang dilewati seperti harus menyimpan dan menghapus query beserta file gambar, saya menggunakan
    tabel agar jika ada banyak proses file yang diakses tidak akan tertukar dengan file orang lain, misal ada berapa orang yang ingin
    menconvert gambar diwaktu bersamaan, jika tidak ditandain dengan nomor dari bigautofield dan hanya menggunakan 1 nama, sangat besar kemungkinan
    gambar akan tertukar, sedangkan jika memanfaatkan table dengan big auto field tidak mungkin tertukar, dan untuk membuatnya lebih efisien
    file yang telah dikelolah dan dikembalikan akan dihapus untuk menjaga API tidak berat, menurut saya algoritma dibawah cukup bagus hanya waktunya
    tidak secepat Convert di atas.

    """
    def post(self,request,format=None):
        rr = True
        try:
            idx = Mode.objects.create(**{"text":"a"})
            x = request.FILES["foto"]
            p = cairosvg.svg2png(file_obj=x, write_to="pops"+str(idx.id)+".png")
            idx.save()
            im = Image.open("pops"+str(idx.id)+".png")
            im = im.resize((int(request.data["width"]),int(request.data["height"])),Image.ANTIALIAS)
            im.save("pops"+str(idx.id)+".png")
            img = open("pops"+str(idx.id)+".png",mode="rb").read()
            Mode.objects.get(id=idx.id).delete()
            os.remove("pops"+str(idx.id)+".png")
        except:
            rr = False
            pass
        if rr:
            return HttpResponse(img,content_type="image/png")
        return Response({"Message":"Bad Request"},status=status.HTTP_400_BAD_REQUEST)

class ConvertFromURL(APIView):
    def post(self,request,format=None):
        """

        fungsi ini hanya dapat digunakan untuk menconvert gambar svg menggunakan link, adapun contoh link yang dapat digunakan seperti:
        "https://freepik.cdnpk.net/img/avatars/01.svg" dan "https://betacssjs.chesscomfiles.com/bundles/web/favicons/safari-pinned-tab.f387b3f2.svg",
        jika diinput selain itu akanmengembalikan bad request.

                                    Mohon Maaf jika Ada Kesalahan, Terimakasih Atas Kesempatannya

        """
        r = True
        try:
            # contents = rr.urlopen("https://freepik.cdnpk.net/img/avatars/01.svg").read()
            # contents = rr.urlopen("https://betacssjs.chesscomfiles.com/bundles/web/favicons/safari-pinned-tab.f387b3f2.svg").read()
            contents = rr.urlopen(request.data["url"]).read()
            document = Document.loadFromData(contents)
            bitmap = document.renderToBitmap()

            svgArray = np.array(bitmap, copy=False)
            img = Image.fromarray(svgArray)
            img = img.resize((int(request.data["width"]),int(request.data["height"])))
            byte_io = io.BytesIO()

            img.save(byte_io, 'PNG')
        except Exception as e:
            print(str(e))
            r = False
            pass
        if r:
            # op = open(byte_io,mode="rb").read()
            return HttpResponse( byte_io.getvalue(), content_type="image/png")
        return Response({"Message": "Error"},status=status.HTTP_400_BAD_REQUEST)