import tkinter as tk
from PIL import Image, ImageTk

class VendingMachine:
    def __init__(self, root):
        self.root = root
        root.title("Vending Machine")

        # Mendapatkan lebar dan tinggi layar
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Menghitung posisi tengah jendela
        x_pos = (screen_width - 500) // 2  # Mengatur lebar jendela menjadi 500 piksel
        y_pos = (screen_height - 750) // 2  # Mengatur tinggi jendela menjadi 600 piksel

        # Menetapkan posisi jendela
        root.geometry(f"500x700+{x_pos}+{y_pos}")

        # Membuat kotak latar belakang dengan warna abu-abu
        self.canvas = tk.Canvas(root, width=300, height=450, bg="#ADD8E6")
        self.canvas.place(x=20, y=50)  # Atur posisi dan ukuran Canvas
   
        # Load the images
        self.image_ayam = Image.open("lawar_ayam.png")
        self.image_babi = Image.open("lawar_babi.png")
        self.image_vegetarian = Image.open("lawar_vegetarian.png")
        
        self.image_5000 = Image.open("5000.png")
        self.image_10000 = Image.open("10000.png")
        self.image_20000 = Image.open("20000.png")
        
        self.image_daging_ayam = Image.open("daging_ayam.png")
        self.image_daging_babi = Image.open("daging_babi.png")
        self.image_daging_vegetarian = Image.open("daging_vegetarian.png")
        
        self.image_sayur_nangka = Image.open("sayur_nangka.png")
        self.image_sayur_kelapa = Image.open("sayur_kelapa.png")
        self.image_sayur_kacang_panjang = Image.open("sayur_kacang_panjang.png")
        self.image_sayur_klungah = Image.open("sayur_klungah.png")
        


        # Resize the images
        self.image_ayam = self.image_ayam.resize((215, 80), Image.ANTIALIAS)
        self.image_babi = self.image_babi.resize((215, 80), Image.ANTIALIAS)
        self.image_vegetarian = self.image_vegetarian.resize((215, 80), Image.ANTIALIAS)
        
        self.image_5000 = self.image_5000.resize((150, 56), Image.ANTIALIAS)
        self.image_10000 = self.image_10000.resize((150, 56), Image.ANTIALIAS)
        self.image_20000 = self.image_20000.resize((150, 56), Image.ANTIALIAS)
        
        self.image_daging_ayam = self.image_daging_ayam.resize((215, 80), Image.ANTIALIAS)
        self.image_daging_babi = self.image_daging_babi.resize((215, 80), Image.ANTIALIAS)
        self.image_daging_vegetarian = self.image_daging_vegetarian.resize((215, 80), Image.ANTIALIAS)
        
        self.image_sayur_nangka = self.image_sayur_nangka.resize((215, 60), Image.ANTIALIAS)
        self.image_sayur_kelapa = self.image_sayur_kelapa.resize((215, 60), Image.ANTIALIAS)
        self.image_sayur_kacang_panjang = self.image_sayur_kacang_panjang.resize((215, 60), Image.ANTIALIAS)
        self.image_sayur_klungah = self.image_sayur_klungah.resize((215, 60), Image.ANTIALIAS)
        
        # Create PhotoImage objects from the resized images
        self.photo_ayam = ImageTk.PhotoImage(self.image_ayam)
        self.photo_babi = ImageTk.PhotoImage(self.image_babi)
        self.photo_vegetarian = ImageTk.PhotoImage(self.image_vegetarian)
        
        self.photo_5000 = ImageTk.PhotoImage(self.image_5000)
        self.photo_10000 = ImageTk.PhotoImage(self.image_10000)
        self.photo_20000 = ImageTk.PhotoImage(self.image_20000)
        
        self.photo_daging_ayam = ImageTk.PhotoImage(self.image_daging_ayam)
        self.photo_daging_babi = ImageTk.PhotoImage(self.image_daging_babi)
        self.photo_daging_vegetarian = ImageTk.PhotoImage(self.image_daging_vegetarian)
        
        self.photo_sayur_nangka = ImageTk.PhotoImage(self.image_sayur_nangka)
        self.photo_sayur_kelapa = ImageTk.PhotoImage(self.image_sayur_kelapa)
        self.photo_sayur_kacang_panjang = ImageTk.PhotoImage(self.image_sayur_kacang_panjang)
        self.photo_sayur_klungah = ImageTk.PhotoImage(self.image_sayur_klungah)
        
        # Create labels to display the images
        self.lbl_5000 = tk.Label(root, image=self.photo_5000)
        self.lbl_10000 = tk.Label(root, image=self.photo_10000)
        self.lbl_20000 = tk.Label(root, image=self.photo_20000)
        
        self.lbl_ayam = tk.Label(root, image=self.photo_ayam)
        self.lbl_babi = tk.Label(root, image=self.photo_babi)
        self.lbl_vegetarian = tk.Label(root, image=self.photo_vegetarian)
        
        self.lbl_daging_ayam = tk.Label(root, image=self.photo_daging_ayam)
        self.lbl_daging_babi = tk.Label(root, image=self.photo_daging_babi)
        self.lbl_daging_vegetarian = tk.Label(root, image=self.photo_daging_vegetarian)
        
        self.lbl_sayur_nangka = tk.Label(root, image=self.photo_sayur_nangka)
        self.lbl_sayur_kelapa = tk.Label(root, image=self.photo_sayur_kelapa)
        self.lbl_sayur_kacang_panjang = tk.Label(root, image=self.photo_sayur_kacang_panjang)
        self.lbl_sayur_klungah = tk.Label(root, image=self.photo_sayur_klungah)
        
        # Place the labels at different positions
        self.lbl_ayam.place(x=60, y=72)
        self.lbl_babi.place(x=60, y=200)
        self.lbl_vegetarian.place(x=60, y=324)
        
        self.lbl_masukkanuang = tk.Label(root, text="MASUKKAN UANG")
        self.lbl_masukkanuang.place(x=348, y=100)
        
        # Create buttons using the images
        self.btn_5000 = tk.Button(root, image=self.photo_5000, command=lambda: self.insert_coin(5))
        self.btn_10000 = tk.Button(root, image=self.photo_10000, command=lambda: self.insert_coin(10))
        self.btn_20000 = tk.Button(root, image=self.photo_20000, command=lambda: self.insert_coin(20))

        # Place the buttons at different positions
        self.btn_5000.place(x=330, y=120)
        self.btn_10000.place(x=330, y=190)
        self.btn_20000.place(x=330, y=260)

        self.state = "Q0"
        self.total_coins = 0
        self.total_kembalian = 0
        self.total_temp = 0
        self.state_history = []
        self.product_price = {"lawar ayam": 25, "lawar babi": 25, "lawar vegetarian": 25, "custom" : 0, "daging" : 0, "sayur" : 0, "Kacang Panjang": 5, "Nangka": 5, "Klungah": 5, "Kelapa": 5, "Daging Babi": 5,"Daging Ayam": 5, "Daging Vegetarian": 5, "Pedas": 0, "Sedang": 0, "Tidak Pedas": 0}
        self.selected_product = []
        
        # Label Status
        self.lbl_status = tk.Label(root, text="Status Mesin: Idle")
        self.lbl_status.place(x=20, y=500)

        self.lbl_product = tk.Label(text=f"Produk: ")
        self.lbl_product.place(x=20, y=530)
        
        # Label Total Uang
        self.lbl_total_uang = tk.Label(root, text="Total Uang: 0k")
        self.lbl_total_uang.place(x=330, y=50)

        # menu Lawar Babi
        self.btn_lawar_babi = tk.Button(root, text="lawar babi", command=lambda: [self.buy_product("lawar babi") and self.choose_seasoning()], width=30, height=1)
        self.btn_lawar_babi.place(x=60, y=152)

        #self.btn lawar ayam
        self.btn_lawar_ayam = tk.Button(root, text="Lawar Ayam", command=lambda: [self.buy_product("lawar ayam")  and self.choose_seasoning()], width=30, height=1)
        self.btn_lawar_ayam.place(x=60, y=280)

        #self.btn lawar vegetarian
        self.btn_lawar_vegetarian = tk.Button(root, text="Lawar Vegetarian", command=lambda: [self.buy_product("lawar vegetarian") and self.choose_seasoning()], width=30, height=1)
        self.btn_lawar_vegetarian.place(x=60, y=404)

        #self.btn custom
        self.btn_custom = tk.Button(root, text="Custom", command =lambda: self.next_menu(), width=30, height=1)
        self.btn_custom.place(x=60, y=452)

        # Tombol Reset
        self.btn_reset = tk.Button(root, text="Reset", command=lambda: self.reset(), width=20, height=2)
        self.btn_reset.place(x=20, y=550)

        # Membuat tombol Confirm Purchase
        self.btn_confirm_purchase = tk.Button(root, text="Confirm Purchase", command= lambda: self.confirm_purchase(), width=20, height=2)
        self.btn_confirm_purchase.place(x=320, y=550)

        self.btn_siap_piring = tk.Button(root, text="Siapkan Piring", command=self.siap_piring, width=20, height=2)
        self.btn_siap_piring.place(x=330, y=459)

        self.btn_cancel = tk.Button(root, text="Cancel", command=lambda: self.cancel(), width=20, height=2)
        self.btn_cancel.place(x=170, y=550)

    def cancel(self):
        if self.state == "S" or self.state == "K" or self.state == "L" or self.state == "M" or self.state == "N":
            self.state = "Q0"
            self.lbl_total_uang.config(text="Total Uang: 0k")
            self.total_coins += self.total_kembalian
            self.lbl_status.config(text=f"Kembalian : {self.total_coins}k (State - Q2)")
            self.total_coins = 0
            self.total_kembalian = 0
            self.selected_product = []
            
    def reset(self):
        if self.state == "D" or self.state == "E" or self.state == "F" or self.state == "G":
            self.state = "R"
            self.total_coins == self.total_temp
            self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
            self.selected_product = []

            self.btn_kacang_panjang.destroy()
            self.btn_klungah.destroy()
            self.btn_kelapa.destroy()
            self.btn_nangka.destroy()
            
            self.btn_bumbu_netral.destroy()
            self.btn_bumbu_sedang.destroy()
            self.btn_bumbu_pedas.destroy()

            # Tampilkan tombol-tombol baru
            # menu Lawar Babi
            self.btn_lawar_babi = tk.Button(root, text="lawar babi", command=lambda: [self.buy_product("lawar babi")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_babi.place(x=60, y=152)

            #self.btn lawar ayam
            self.btn_lawar_ayam = tk.Button(root, text="Lawar Ayam", command=lambda: [self.buy_product("lawar ayam")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_ayam.place(x=60, y=280)

            #self.btn lawar vegetarian
            self.btn_lawar_vegetarian = tk.Button(root, text="Lawar Vegetarian", command=lambda: [self.buy_product("lawar vegetarian") and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_vegetarian.place(x=60, y=404)

            #self.btn custom
            self.btn_custom = tk.Button(root, text="Custom", command =lambda: self.next_menu(), width=30, height=1)
            self.btn_custom.place(x=60, y=452)

        elif self.state == "H" or self.state == "I" or self.state == "J":
            self.state = "R"
            self.total_coins == self.total_temp
            self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
            self.selected_product = []

            self.btn_daging_ayam.destroy()
            self.btn_daging_babi.destroy()
            self.btn_daging_vegetarian.destroy()

            # Tampilkan tombol-tombol baru
            # menu Lawar Babi
            self.btn_lawar_babi = tk.Button(root, text="lawar babi", command=lambda: [self.buy_product("lawar babi")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_babi.place(x=60, y=152)

            #self.btn lawar ayam
            self.btn_lawar_ayam = tk.Button(root, text="Lawar Ayam", command=lambda: [self.buy_product("lawar ayam")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_ayam.place(x=60, y=280)

            #self.btn lawar vegetarian
            self.btn_lawar_vegetarian = tk.Button(root, text="Lawar Vegetarian", command=lambda: [self.buy_product("lawar vegetarian") and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_vegetarian.place(x=60, y=404)

            #self.btn custom
            self.btn_custom = tk.Button(root, text="Custom", command =lambda: self.next_menu(), width=30, height=1)
            self.btn_custom.place(x=60, y=452)

        elif self.state == "K" or self.state == "L" or self.state == "M" or self.state =="A" or self.state =="B" or self.state =="C":
            self.state = "R"
            self.total_coins == self.total_temp
            self.lbl_status.config(text=f"Idle(State - {self.state} )")
            self.selected_product = []

            self.btn_bumbu_pedas.destroy()
            self.btn_bumbu_sedang.destroy()
            self.btn_bumbu_netral.destroy()

            # Tampilkan tombol-tombol baru
            # Place the labels at different positions
            self.lbl_ayam.place(x=60, y=72)
            self.lbl_babi.place(x=60, y=200)
            self.lbl_vegetarian.place(x=60, y=324)
        
            # menu Lawar Babi
            self.btn_lawar_babi = tk.Button(root, text="lawar babi", command=lambda: [self.buy_product("lawar babi")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_babi.place(x=60, y=152)

            #self.btn lawar ayam
            self.btn_lawar_ayam = tk.Button(root, text="Lawar Ayam", command=lambda: [self.buy_product("lawar ayam")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_ayam.place(x=60, y=280)

            #self.btn lawar vegetarian
            self.btn_lawar_vegetarian = tk.Button(root, text="Lawar Vegetarian", command=lambda: [self.buy_product("lawar vegetarian") and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_vegetarian.place(x=60, y=404)

            #self.btn custom
            self.btn_custom = tk.Button(root, text="Custom", command =lambda: self.next_menu(), width=30, height=1)
            self.btn_custom.place(x=60, y=452)
            
        elif self.state == "P":
            self.state = "Q0"
            self.total_coins == self.total_temp
            self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
            self.selected_product = []

            self.btn_bumbu_pedas.destroy()
            self.btn_bumbu_sedang.destroy()
            self.btn_bumbu_netral.destroy()

            # Tampilkan tombol-tombol baru
            # Place the labels at different positions
            self.lbl_ayam.place(x=60, y=72)
            self.lbl_babi.place(x=60, y=200)
            self.lbl_vegetarian.place(x=60, y=324)
        
            # menu Lawar Babi
            self.btn_lawar_babi = tk.Button(root, text="lawar babi", command=lambda: [self.buy_product("lawar babi")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_babi.place(x=60, y=152)

            #self.btn lawar ayam
            self.btn_lawar_ayam = tk.Button(root, text="Lawar Ayam", command=lambda: [self.buy_product("lawar ayam")  and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_ayam.place(x=60, y=280)

            #self.btn lawar vegetarian
            self.btn_lawar_vegetarian = tk.Button(root, text="Lawar Vegetarian", command=lambda: [self.buy_product("lawar vegetarian") and self.choose_seasoning()], width=30, height=1)
            self.btn_lawar_vegetarian.place(x=60, y=404)

            #self.btn custom
            self.btn_custom = tk.Button(root, text="Custom", command =lambda: self.next_menu(), width=30, height=1)
            self.btn_custom.place(x=60, y=452)

        elif self.state == "R":
            self.lbl_status.config(text=f"Silahkan memilih Pilihan Menu")
            
    def insert_coin(self, coin):
        if self.total_coins + coin <= 25:
            if coin == 5 and self.state == "Q0":
                self.state = "S"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 5 and self.state == "S":
                self.state = "K"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 5 and self.state == "K":
                self.state = "L"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")    
            elif coin == 5 and self.state == "L":
                self.state = "M"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 5 and self.state == "M":
                self.state = "N"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 5 and self.state == "N":
                self.state = "N"
                self.total_kembalian += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 10 and self.state == "Q0":
                self.state = "K"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 10 and self.state == "S":
                self.state = "L"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 10 and self.state == "K":
                self.state = "M"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 10 and self.state == "L":
                self.state = "N"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 10 and self.state == "M":
                self.state = "N"
                self.total_coins += 5
                self.total_kembalian += 5
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 10 and self.state == "N":
                self.state = "N"
                self.total_kembalian += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 20 and self.state == "Q0":
                self.state = "M"
                self.total_coins += coin
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 20 and self.state == "S":
                self.state = "N"
                self.total_coins += 20
                self.total_kembalian += 0
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 20 and self.state == "K":
                self.state = "N"
                self.total_coins += 15
                self.total_kembalian += 5
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 20 and self.state == "L":
                self.state = "N"
                self.total_coins += 10
                self.total_kembalian += 10
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 20 and self.state == "M":
                self.state = "N"
                self.total_coins += 5
                self.total_kembalian += 15
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
            elif coin == 20 and self.state == "N":
                self.state = "N"
                self.total_coins += 0
                self.total_kembalian += 20
                self.total_temp = self.total_coins
                self.lbl_status.config(text=f"Status Mesin: AcceptingCoins (State - {self.state} )")
                self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}k")
        else:
            self.lbl_status.config(text=f"UANG MELEBIHI 25K")
                
    def buy_product(self, product):
        if self.state == "R":   
            if product in self.product_price and product == "lawar ayam":
                if self.total_coins >= self.product_price[product]:
                    self.state = "A"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "lawar babi":
                if self.total_coins >= self.product_price[product]:
                    self.state = "B"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "lawar vegetarian":
                if self.total_coins >= self.product_price[product]:
                    self.state = "C"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "custom":
                if self.total_coins >= self.product_price[product]:
                    self.state = "O"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product} (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
                    
        elif self.state == "O" :
            if product in self.product_price and product == "Kacang Panjang":
                if self.total_coins >= self.product_price[product]:
                    self.state = "D"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")                    
            elif product in self.product_price and product == "Klungah":
                if self.total_coins >= self.product_price[product]:
                    self.state = "F"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "Nangka":
                if self.total_coins >= self.product_price[product]:
                    self.state = "E"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "Kelapa":
                if self.total_coins >= self.product_price[product]:
                    self.state = "G"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
                    
        elif self.state == "D" or self.state == "E" or self.state == "F" or self.state == "G"  :
            if product in self.product_price and product == "Kacang Panjang":
                if self.total_coins >= self.product_price[product]:
                    self.state = "D"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")                    
            elif product in self.product_price and product == "Klungah":
                if self.total_coins >= self.product_price[product]:
                    self.state = "F"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "Nangka":
                if self.total_coins >= self.product_price[product]:
                    self.state = "E"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "Kelapa":
                if self.total_coins >= self.product_price[product]:
                    self.state = "G"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            elif product in self.product_price and product == "daging":
                if self.total_coins >= self.product_price[product]:
                    self.state = "T"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product} (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
        
        elif self.state == "T": 
            if product in self.product_price and product == "Daging Babi":
                if self.total_coins >= self.product_price[product]:
                    self.state = "I"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi") 
                    
            if product in self.product_price and product == "Daging Ayam":
                if self.total_coins >= self.product_price[product]:
                    self.state = "H"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
                    
            if product in self.product_price and product == "Daging Vegetarian":
                if self.total_coins >= self.product_price[product]:
                    self.state = "J"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")

        elif self.state == "H" or self.state == "I" or self.state == "J" : 
            if product in self.product_price and product == "Daging Babi":
                if self.total_coins >= self.product_price[product]:
                    self.state = "I"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi") 
                    
            elif product in self.product_price and product == "Daging Ayam":
                if self.total_coins >= self.product_price[product]:
                    self.state = "H"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
                    
            elif product in self.product_price and product == "Daging Vegetarian":
                if self.total_coins >= self.product_price[product]:
                    self.state = "J"
                    self.selected_product.append(product)  
                    self.total_temp == self.total_coins
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")

        elif self.state == "A" or self.state == "B" or self.state == "C" or self.state == "H" or self.state == "I" or self.state == "J" or self.state == "P":
            if product in self.product_price and product == "Pedas":
                if self.total_coins >= self.product_price[product]:
                    self.state = "P"
                    self.selected_product.append(product)  
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            if product in self.product_price and product == "Sedang":
                if self.total_coins >= self.product_price[product]:
                    self.state = "P"
                    self.selected_product.append(product)  
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")
            if product in self.product_price and product == "Tidak Pedas":
                if self.total_coins >= self.product_price[product]:
                    self.state = "P"
                    self.selected_product.append(product)  
                    self.total_coins -= self.product_price[product] 
                    self.lbl_status.config(text=f"Status Mesin: Dispensing - ({product}({self.product_price[product]}) (State - {self.state} ))")
                    self.lbl_total_uang.config(text=f"Total Uang: {self.total_coins}")
                    return f"Produk {product} telah dipilih. Sisa uang: {self.total_coins}"
                else:
                    self.lbl_status.config(text="Uang Tidak Mencukupi")

    def confirm_purchase(self):
        if self.selected_product and self.state == "P":
            total_cost = 0
            if self.total_coins >= total_cost:
                product_purchased = ", ".join(self.selected_product)
                self.selected_product = []  # Mengosongkan list produk yang dipilih
                self.total_kembalian += self.total_coins 
                self.lbl_status.config(text=f"Pembelian Berhasil, Kembalian : {self.total_kembalian}k")
                self.lbl_product.config(text=f"Produk: {product_purchased}")
                self.lbl_total_uang.config(text="Total Uang: 0k")
                self.total_coins = 0
                self.total_kembalian = 0 
                return f"Pembelian {product_purchased} berhasil dikonfirmasi."
            else:
                self.lbl_status.config(text="Koin tidak mencukupi untuk produk ini.")
        else:
            return "Tidak ada produk yang dipilih atau transaksi belum selesai."

    def siap_piring(self):
        if self.state == "M" or self.state == "N":
            self.state = "R"
            self.lbl_status.config(text=f"Piring Disiapkan (State - R)")
        else:
            if self.state == "R":
                self.lbl_status.config(text="Piring Sudah Disiapkan!")  
            else:
                self.lbl_status.config(text="Koin Belum Dimasukkan!")     
               
    def next_menu (self):
        # Hilangkan tombol-tombol sebelumnya
        self.btn_lawar_vegetarian.destroy()
        self.btn_lawar_babi.destroy()
        self.btn_custom.destroy()
        self.btn_lawar_ayam.destroy()
        # Remove the labels
        self.lbl_ayam.place_forget()
        self.lbl_babi.place_forget()
        self.lbl_vegetarian.place_forget()
        
        self.lbl_sayur_kacang_panjang.place(x=60, y=76)
        self.lbl_sayur_kelapa.place(x=60, y=185)
        self.lbl_sayur_nangka.place(x=60, y=294)
        self.lbl_sayur_klungah.place(x=60, y=403)
        
        self.state = "O"
        self.lbl_status.config(text=f"Menyiapkan Sayuran - (State - {self.state} ))")

        # Tampilkan tombol-tombol baru
        self.btn_kacang_panjang = tk.Button(root, text="Kacang Panjang", command=lambda: self.buy_product("Kacang Panjang"), width=30, height=1)
        self.btn_kacang_panjang.place(x=60, y=136)

        self.btn_klungah = tk.Button(root, text="Klungah", command=lambda: self.buy_product("Klungah"), width=30, height=1)
        self.btn_klungah.place(x=60, y=245)

        self.btn_nangka = tk.Button(root, text="Nangka", command=lambda: self.buy_product("Nangka"), width=30, height=1)
        self.btn_nangka.place(x=60, y=354)

        self.btn_kelapa = tk.Button(root, text="Kelapa", command=lambda: self.buy_product("Kelapa"), width=30, height=1)
        self.btn_kelapa.place(x=60, y=463)

        self.btn_next2 = tk.Button(root, text="next", command=self.next_menu_2, width=20, height=2)
        self.btn_next2.place(x=330, y=403)
    
    def next_menu_2(self):
        # Hilangkan tombol-tombol sebelumnya
        self.btn_kelapa.destroy()
        self.btn_kacang_panjang.destroy()
        self.btn_nangka.destroy()
        self.btn_klungah.destroy()
        self.btn_next2.destroy()
        
        self.lbl_sayur_kacang_panjang.place_forget()
        self.lbl_sayur_kelapa.place_forget()
        self.lbl_sayur_klungah.place_forget()
        self.lbl_sayur_nangka.place_forget()
        
        self.lbl_daging_ayam.place(x=60, y=72)
        self.lbl_daging_babi.place(x=60, y=200)
        self.lbl_daging_vegetarian.place(x=60, y=324)
        
        self.state = "T"
        self.lbl_status.config(text=f"Status Mesin: Menyiapkan Daging - (State - {self.state} ))")

        # Tampilkan tombol-tombol baru
        self.btn_daging_babi = tk.Button(root, text="Daging Babi", command=lambda: self.buy_product("Daging Babi"), width=30, height=1)
        self.btn_daging_babi.place(x=60, y=152)

        self.btn_daging_ayam = tk.Button(root, text="Daging Ayam", command=lambda: self.buy_product("Daging Ayam"), width=30, height=1)
        self.btn_daging_ayam.place(x=60, y=280)

        self.btn_daging_vegetarian = tk.Button(root, text="Daging vegetarian", command=lambda: self.buy_product("Daging Vegetarian"), width=30, height=1)
        self.btn_daging_vegetarian.place(x=60, y=404)

        self.btn_next_3 = tk.Button(root, text="next", command=self.next_menu_3, width=20, height=2)
        self.btn_next_3.place(x=330, y=463)

    def next_menu_3(self):
        # Hilangkan tombol-tombol sebelumnya
        self.btn_daging_ayam.destroy()
        self.btn_daging_babi.destroy()
        self.btn_daging_vegetarian.destroy()
        
        self.lbl_daging_ayam.place_forget()
        self.lbl_daging_babi.place_forget()
        self.lbl_daging_vegetarian.place_forget()
        
        self.state = "P"
        
        self.btn_bumbu_pedas = tk.Button(root, text="Bumbu Pedas", command=lambda: self.buy_product("Pedas"), width=30, height=1)
        self.btn_bumbu_pedas.place(x=60, y=100)

        self.btn_bumbu_sedang = tk.Button(root, text="Bumbu Sedang", command=lambda: self.buy_product("Sedang"), width=30, height=1)
        self.btn_bumbu_sedang.place(x=60, y=200)

        self.btn_bumbu_netral = tk.Button(root, text="Bumbu Tidak Pedas", command=lambda: self.buy_product("Tidak Pedas"), width=30, height=1)
        self.btn_bumbu_netral.place(x=60, y=300)

    def choose_seasoning(self):
        # Hilangkan tombol-tombol sebelumnya
        self.btn_lawar_vegetarian.destroy()
        self.btn_lawar_babi.destroy()
        self.btn_custom.destroy()
        self.btn_lawar_ayam.destroy()
        
        # Remove the labels
        self.lbl_ayam.place_forget()
        self.lbl_babi.place_forget()
        self.lbl_vegetarian.place_forget()

        self.btn_bumbu_pedas = tk.Button(root, text="Bumbu Pedas", command=lambda: self.buy_product("Pedas"), width=30, height=1)
        self.btn_bumbu_pedas.place(x=60, y=100)

        self.btn_bumbu_sedang = tk.Button(root, text="Bumbu Sedang", command=lambda: self.buy_product("Sedang"), width=30, height=1)
        self.btn_bumbu_sedang.place(x=60, y=200)

        self.btn_bumbu_netral = tk.Button(root, text="Bumbu Tidak Pedas", command=lambda: self.buy_product("Tidak Pedas"), width=30, height=1)
        self.btn_bumbu_netral.place(x=60, y=300)

if __name__ == "__main__":
    root = tk.Tk()
    vending_machine = VendingMachine(root)
    root.mainloop()
