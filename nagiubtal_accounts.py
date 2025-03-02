from customtkinter import *
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import ttk, messagebox
import json
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root =CTk()
root.iconbitmap(resource_path("icon.ico"))
root.geometry("750x695+0+0")
root.title("حسابات نجيبتال")
root.resizable(False ,True )



set_default_color_theme("green")


#frame1
frame1=CTkFrame(master=root,fg_color="#4c4544",corner_radius=0)
frame1.pack(fill=Y,expand=True,anchor='w')


def price_editing():
# Load the JSON data from a file
    with open('prices.json', 'r', encoding='utf-8') as file:
        product_prices = json.load(file)
    
    # Create the main application window
    app = tk.Tk()
    app.title("Product Prices")
    
    # Create a frame to hold the treeviews and scrollbars
    frame = tk.Frame(app)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas for scrolling
    canvas = tk.Canvas(frame)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    # Configure the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    # Create a window in the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack the canvas and scrollbar
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Create a label and treeview for each category
    trees = {}  # To hold references to the treeviews for later access
    for category, products in product_prices.items():
        # Create a label for the category
        category_label = tk.Label(scrollable_frame, text=category, font=('Arial', 14, 'bold'))
        category_label.pack(pady=10)
    
        # Create a treeview for the products
        tree = ttk.Treeview(scrollable_frame, columns=('Product', 'Price'), show='headings')
        tree.heading('Product', text='Product')
        tree.heading('Price', text='Price')
        tree.pack(fill=tk.BOTH, expand=True)
    
        # Store the treeview in the dictionary for later access
        trees[category] = tree
    
        # Insert products into the treeview
        for product, price in products.items():
            tree.insert('', 'end', values=(product, price))
    
        # Add a separator between categories
        separator = ttk.Separator(scrollable_frame, orient='horizontal')
        separator.pack(fill='x', pady=10)
    
    # Function to update the price
    def update_price():
        # Get the selected item from each tree until one is found
        selected_item, selected_tree = None, None
        for category, tree in trees.items():
            selected_item = tree.selection()
            if selected_item:
                selected_tree = tree
                break
        
        if selected_item:
            # Get the new price from the entry
            new_price = price_entry.get()
            
            # Validate the new price
            try:
                float(new_price)  # Convert to float to validate
            except ValueError:
                messagebox.showerror("خطاْ", "يرجى ادخال رقم")
                return
           
            # Get the product name to match it in the JSON structure
            product = selected_tree.item(selected_item)['values'][0]
            
            # Update the selected item's price in the Treeview
            selected_tree.item(selected_item, values=(product, new_price))
            
            # Update the price in the JSON data for the correct category
            for category, products in product_prices.items():
                if product in products:
                    product_prices[category][product] = new_price
                    break
            
            # Save the updated JSON data back to the file
            with open('prices.json', 'w', encoding='utf-8') as file:
                json.dump(product_prices, file, ensure_ascii=False, indent=4)
            
            messagebox.showinfo("تم بنجاح", f" {new_price} ل {product}تم تحديث سعر ")
        else:
            messagebox.showwarning("خطاْ", "يرجى اختيار منتج لتعديله")

    # Entry for new price
    price_entry = tk.Entry(app)
    price_entry.pack(pady=10)
    
    # Button to update the price
    update_button = tk.Button(app, text="Update Price", command=update_price)
    update_button.pack(pady=5)
    
    # Start the application
    app.mainloop()




def remove_indicator():
    account_indicator1.configure(bg_color="#4c4544",fg_color="#4c4544")
    account_indicator2.configure(bg_color="#4c4544",fg_color="#4c4544")
    account_indicator3.configure(bg_color="#4c4544",fg_color="#4c4544")




def indicator(lb):
    remove_indicator()
    lb.configure(bg_color="black",fg_color="black")







#indicates
account_indicator1=CTkLabel(master=frame1,text=" ",bg_color="black",fg_color="black",height=40)
account_indicator1.place(x=15,y=50)

account_indicator2=CTkLabel(master=frame1,text=" ",bg_color="#4c4544",fg_color="#4c4544",height=40)
account_indicator2.place(x=15,y=200)

account_indicator3=CTkLabel(master=frame1,text=" ",bg_color="#4c4544",fg_color="#4c4544",height=40)
account_indicator3.place(x=15,y=350)



#products


product_classes=["أکسسوار P.s","كرانن", 
"أكسسوار چامبو و تانجو"
,
"مجرى درج"
,
"کاوتش"
,
"تنده"
,
"سلك فيبر"
,
"أكسسوار السعد"
,
"سلك صلب"
,
"کوالین"
,
"مفصلات مطابخ"
,
"مقابض"
,
"صفایات"
,
"فرش"
,
"مسامير"
,
"بنط "
,
"عظم مطابخ"
,
"باقى أكسسوار مطابخ"
,
"الانكيه و فشر"
,
"اكسسوارات أخرى"
,
"منتجات الكينج ابيض"
,
"منتجات الكينج اسود وبيج"
,
"تروال زيت"
,
"الموتال"
,
"فيبر و كلادينج"]



def combined_commands():
    price_editing()

    
def combined_commands2():
    child_widgets=frame2.winfo_children()
    for child in child_widgets:
        child.destroy()
    indicator(account_indicator1)
    make_account()

def combined_commands3():
    child_widgets=frame2.winfo_children()
    for child in child_widgets:
        child.destroy()
    indicator(account_indicator3)
    edit_produts()

# Buttons1

button1 = CTkButton(master=frame1, 
                    text="اضافة حسابات", 
                    fg_color="#4c4544",  
                    text_color="white",  
                    border_width=0,  
                    corner_radius=0, 
                    hover_color="black", 
                    font=("Rubic", 30),
                    command=combined_commands2)
button1.place(x=20,y=50) 


button2 = CTkButton(master=frame1, 
                    text="الاسعار", 
                    fg_color="#4c4544", 
                    text_color="white", 
                    border_width=0, 
                    corner_radius=0,  
                    hover_color="black",  #
                    font=("Rubic", 30),
                    command=combined_commands)
button2.place(x=20,y=200) 

button3 = CTkButton(master=frame1, 
                    text="قاىْمة المنتجات", 
                    fg_color="#4c4544", 
                    text_color="white", 
                    border_width=0, 
                    corner_radius=0,  
                    hover_color="black",  #
                    font=("Rubic", 30),
                    command=combined_commands3
                    )
button3.place(x=20,y=350) 

#frame2
frame2=CTkFrame(master=root,fg_color="#2A2A2A",corner_radius=0,height=3000,width=550)
frame2.place(x=200,y=0)



def make_account():
    # نفترض أن لديك ملف الـ JSON الخاص بالمنتجات محمل مسبقاً
    with open('prices.json', 'r', encoding='utf-8') as f:
        products_data = json.load(f)
    
    def showing_price():
        selected_category = grandson_combobox1.get()  # Get the selected category (section) from combobox1
        selected_product = grandson_combobox2.get()  # Get the selected product from combobox2
        price_times = grandson_entry5.get()  # Get the quantity from the entry
    
        # Ensure that a category is selected
        if selected_category == "اختر القسم":
            CTkMessagebox(title="ERROR", message="يرجى اختيار قسم", icon="cancel")
            return
    
        # Ensure that a product is selected
        if selected_product == "اختر المنتج":
            CTkMessagebox(title="ERROR", message="يرجى اختيار منتج", icon="cancel")
            return
    
        # Check if the selected category exists in the JSON data
        if selected_category not in products_data:
            CTkMessagebox(title="ERROR", message="القسم المحدد غير موجود", icon="cancel")
            return
    
        # Now search for the selected product in the chosen category
        category_data = products_data[selected_category]
        price = category_data.get(selected_product, None)
    
        # If the product doesn't exist, show an error
        if price is None:
            CTkMessagebox(title="ERROR", message="المنتج المحدد غير موجود في القسم", icon="cancel")
            return
    
        # Handle quantity calculation
        if price_times:  # Check if quantity is entered
            try:
                quantity = float(price_times)  # Convert quantity to float
                end_price = float(price) * quantity  # Calculate total price
                price_text = f"{end_price:.2f} = {price} * {quantity}: السعر \n{selected_product}: المنتج\n"
            except ValueError:
                CTkMessagebox(title="ERROR", message="يرجى إدخال رقم صحيح في خانة الكمية", icon="cancel")
                return  # Exit if the quantity is invalid
        else:
            # No quantity provided, show only the price of the product
            end_price = float(price)  # Set end_price to the product's price for total calculation
            price_text = f"{selected_product}: المنتج \n{price}: السعر\n"
    
        # Clear the quantity entry field for next use
        grandson_entry5.delete(0, END)
        price_var.set(price)  # Update the price displayed

        # Insert the calculated price text into the textbox
        textbox1.insert(END, price_text)
        textbox1.insert(END, "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    
        # Add to total price calculation in textbox2
        if price_times:
            textbox2.insert(END, f"{end_price} +\n")  # Append the calculated price
        else:
            textbox2.insert(END, f"{price} +\n")  # Append the price of the product
    

    #frame3
    def make_new_day():
        year=grandson_entry1.get()
        month=grandson_entry2.get()
        day=grandson_entry3.get()
        textbox1.insert(END,f"حسابات لسنة {year} شهر {month} يوم {day}\n")
        textbox1.insert(END,"************************************************************\n")

    def add_name():
        name=grandson_entry4.get()
        textbox1.insert(END,f"اسم صاحب الطلبية:{name}\n")
        textbox1.insert(END,"========================>\n")


    def delete_all_products():
        textbox1.delete("0.0",END)
        textbox2.delete("0.0",END)

    def delete_one_products():
        lines = textbox1.get("1.0", END).splitlines()  # الحصول على النص كسطور
        lines2=textbox2.get("1.0", END).splitlines()
        if len(lines) >= 3:
            # مسح محتويات الصندوق
            textbox1.delete("1.0", END)
            # إعادة إدخال النص بدون آخر 3 سطور
            new_text = "\n".join(lines[:-5])
            new_underine="\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
            textbox1.insert(END, new_text)
            textbox1.insert(END, new_underine)
        
        if lines2:
            textbox2.delete("1.0",END)
            new_text2="\n".join(lines2[:-2])
            textbox2.insert(END, f"{new_text2}\n")




    def calculate():
        # Get the current text from textbox2
        calculate_text = textbox2.get("1.0", END)  # Get text and trim whitespace
        calculate_num = calculate_text.splitlines()  # Split text into lines
        calculate_all = " ".join(calculate_num)  # Join lines into a single string
        calculate_all2 = calculate_all.strip()  # Trim whitespace
    
        # Remove the last character if it's not empty
        if calculate_all2:  # Check if there is any text
            calculate_all2 = calculate_all2[:-1]  # Remove the last character
        
        # Evaluate the expression and handle potential errors
        try:
            result = eval(calculate_all2)  # Evaluate the expression
            # Format result to two decimal places
            formatted_result = f"{result:.2f}"
            
            # Insert the result into textbox1
            textbox1.insert(END, "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")  # Separator
            textbox1.insert(END, "المجموع هو\n")
            textbox1.insert(END, formatted_result)
        except Exception as e:
            CTkMessagebox(title="ERORR", message="لاحسبها اسعار تكتب لم", icon="cancel")  # Error message
        
    def update_product_list(category):
        # Ensure the category exists in the products_data
        if category in products_data:
        # Get all product names for the selected category
            product_names = list(products_data[category].keys())
        # Update the values in grandson_combobox2
            grandson_combobox2.configure(values=product_names)
        else:
        # If the category doesn't exist, clear the combobox
            grandson_combobox2.configure(values=[])


    frame3=CTkFrame(master=frame2,fg_color="#2A2A2A",corner_radius=0,height=3000,width=550)
    frame3.place(x=0,y=0)
    
    child_frame1=CTkFrame(master=frame3,fg_color="black",width=550,height=100,corner_radius=0)
    child_frame1.place(x=0,y=0)
    
    textbox1=CTkTextbox(master=frame3,fg_color="white",width=500,height=575,text_color="black",font=("Rubik",20))
    textbox1.place(x=25,y=110)
    
    textbox2=CTkTextbox(master=frame1,fg_color="white",text_color="black",width=190,height=140,font=("Rubik",20))
    textbox2.place(x=5,y=550)
    
    grandson_label1=CTkLabel(master=child_frame1,bg_color="black",text=":قسم",font=("Rubik",25),text_color="white")
    grandson_label1.place(x=510)
    
    grandson_label2=CTkLabel(master=child_frame1,bg_color="black",text=":المنتج",font=("Rubik",25),text_color="white")
    grandson_label2.place(x=498,y=35)
    
    grandson_label3=CTkLabel(master=child_frame1,bg_color="black",text=":سنة",font=("Rubik",20),text_color="white")
    grandson_label3.place(x=233)
    
    grandson_label4=CTkLabel(master=child_frame1,bg_color="black",text=":شهر",font=("Rubik",20),text_color="white")
    grandson_label4.place(x=122)
    
    grandson_label5=CTkLabel(master=child_frame1,bg_color="black",text=":يوم",font=("Rubik",20),text_color="white")
    grandson_label5.place(x=35)
    
    grandson_label6=CTkLabel(master=child_frame1,bg_color="black",text=":اْلاسم",font=("Rubik",20),text_color="white")
    grandson_label6.place(x=225,y=35)
   
    grandson_label7=CTkLabel(master=child_frame1,bg_color="black",text=":العدد",font=("Rubik",20),text_color="white")
    grandson_label7.place(x=300,y=70)
    
    grandson_combobox1=CTkComboBox(master=child_frame1,fg_color='white',bg_color="black",text_color="black",font=("Rubik",20),values=product_classes,command=update_product_list)
    grandson_combobox1.place(x=360)
    grandson_combobox1.set("اختر القسم")
    
    grandson_combobox2=CTkComboBox(master=child_frame1,fg_color='white',bg_color="black",text_color="black",width=175,font=("Rubik",20))
    grandson_combobox2.place(x=325,y=35)
    grandson_combobox2.set("اختر المنتج")

    grandson_btn1=CTkButton(master=child_frame1,text="يوم جديد",font=("Rubik",20),width=25,hover_color="blue",command=make_new_day)
    grandson_btn1.place(x=275)
    
    grandson_btn2=CTkButton(master=child_frame1,text="اْضافة اسم",font=("Rubik",20),width=25,hover_color="blue",command=add_name)
    grandson_btn2.place(x=3,y=35)
    
    grandson_btn3=CTkButton(master=child_frame1,text="احسب",font=("Rubik",20),width=25,hover_color="blue",command=calculate)
    grandson_btn3.place(x=430,y=70)
    
    grandson_btn4=CTkButton(master=child_frame1,text="اضافة",font=("Rubik",20),width=25,hover_color="blue",command=showing_price)
    grandson_btn4.place(x=200,y=70)
    
    grandson_btn5=CTkButton(master=child_frame1,text="مسح الكل",font=("Rubik",20),width=25,hover_color="blue",command=delete_all_products)
    grandson_btn5.place(x=110,y=70)
    
    grandson_btn6=CTkButton(master=child_frame1,text="مسح اخر منتج",font=("Rubik",20),width=25,hover_color="blue",command=delete_one_products)
    grandson_btn6.place(x=2,y=70)

    grandson_entry1=CTkEntry(master=child_frame1,fg_color="white",bg_color="black",text_color="black",width=40)
    grandson_entry1.place(x=188)

    grandson_entry2=CTkEntry(master=child_frame1,fg_color="white",bg_color="black",text_color="black",width=30)
    grandson_entry2.place(x=90)
    
    grandson_entry3=CTkEntry(master=child_frame1,fg_color="white",bg_color="black",text_color="black",width=30)
    grandson_entry3.place(x=3)
    
    grandson_entry4=CTkEntry(master=child_frame1,fg_color="white",bg_color="black",text_color="black",font=("Rubik",20))
    grandson_entry4.place(x=85,y=35)
      

# grandson_entry5.bind("<Button-1>", keypad)
    def keypad(event=None):
        
        def append_digit(digit):
            current_text = grandson_entry5.get()
            grandson_entry5.delete(0, tk.END)
            grandson_entry5.insert(tk.END, current_text + str(digit))
        
        def delete_one():
            current_text = grandson_entry5.get()
            grandson_entry5.delete(0, tk.END)
            grandson_entry5.insert(tk.END, current_text[:-1])

        def delete_all():
            grandson_entry5.delete(0, tk.END)
        
        keypad = tk.Tk()
        keypad.geometry("290x330")
        keypad.resizable(False, False)
        keypad.title("Keypad")
    
        btn_one=tk.Button(keypad,text="1",width=12,height=3, command=lambda: append_digit(1))
        btn_one.place(x=1,y=1)
        
        btn_two=tk.Button(keypad,text="2",width=12,height=3, command=lambda: append_digit(2))
        btn_two.place(x=98,y=1)
        
        btn_three=tk.Button(keypad,text="3",width=12,height=3, command=lambda: append_digit(3))
        btn_three.place(x=195,y=1)
        
        btn_four=tk.Button(keypad,text="4",width=12,height=3, command=lambda: append_digit(4))
        btn_four.place(x=1,y=60)

        btn_five=tk.Button(keypad,text="5",width=12,height=3, command=lambda: append_digit(5))
        btn_five.place(x=98,y=60)
        
        btn_six=tk.Button(keypad,text="6",width=12,height=3, command=lambda: append_digit(6))
        btn_six.place(x=195,y=60)
        
        btn_seven=tk.Button(keypad,text="7",width=12,height=3, command=lambda: append_digit(7))
        btn_seven.place(x=1,y=119)
        
        btn_eigth=tk.Button(keypad,text="8",width=12,height=3, command=lambda: append_digit(8))
        btn_eigth.place(x=98,y=119)
        
        btn_nine=tk.Button(keypad,text="9",width=12,height=3, command=lambda: append_digit(9))
        btn_nine.place(x=195,y=119)
        
        btn_zero=tk.Button(keypad,text="0",width=12,height=3, command=lambda: append_digit(0))
        btn_zero.place(x=98,y=178)
        
        btn_dot=tk.Button(keypad,text=".",width=12,height=3, command=lambda: append_digit(str(".")))
        btn_dot.place(x=98,y=253)

        delete_one_btn=tk.Button(keypad,text="مسح واحدة",width=12,height=3, command=delete_one)
        delete_one_btn.place(x=1,y=178)

        delete_all_btn=tk.Button(keypad,text="مسح الكل",width=12,height=3, command=delete_all)
        delete_all_btn.place(x=195,y=178)
        keypad.mainloop()


    grandson_entry5=CTkEntry(master=child_frame1,fg_color="white",bg_color="black",text_color="black",width=35)
    grandson_entry5.place(x=260,y=70)
    grandson_entry5.bind("<Button-1>", keypad)



def edit_produts():
    frame4=CTkFrame(master=frame2,fg_color="#2A2A2A",corner_radius=0,height=3000,width=550)
    frame4.place(x=0,y=0)
  
    frame4_label1=CTkLabel(master=frame4,text=":القسم" , font=("Rubik",50), text_color="white",bg_color="#2A2A2A")
    frame4_label1.place(x=450,y=45)

    frame4_label2=CTkLabel(master=frame4,text=":اكتب اسم المنتج" , font=("Rubik",50), text_color="white",bg_color="#2A2A2A")
    frame4_label2.place(x=280,y=205)

    frame4_label3=CTkLabel(master=frame4,text=":اكتب سعر المنتج" , font=("Rubik",50), text_color="white",bg_color="#2A2A2A")
    frame4_label3.place(x=275,y=365)


    frame4_combobox=CTkComboBox(master=frame4,values=product_classes,width=200,height=40)
    frame4_combobox.place(x=50,y=50)
    frame4_combobox.set("القسم اختيار يرجى")

    frame4_entry1=CTkEntry(master=frame4,fg_color="white",text_color="black",font=("Rubik",25),width=250)
    frame4_entry1.place(x=25,y=215)

    frame4_entry2=CTkEntry(master=frame4,fg_color="white",text_color="black",font=("Rubik",25),width=250)
    frame4_entry2.place(x=25,y=370)
 
    # وظيفة لتحميل البيانات من ملف JSON
    def load_data(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return {}

# وظيفة لحفظ البيانات إلى ملف JSON
    def save_data(json_file, data):
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    # وظيفة لإضافة منتج جديد إلى قسم معين
    def add_product(json_file, category, product_name, product_price):
        data = load_data(json_file)
    
        if category not in data:
            data[category] = {}
    
        data[category][product_name] = product_price
        save_data(json_file, data)
        print(f"تم إضافة المنتج '{product_name}' بسعر {product_price} إلى قسم '{category}'.")
    
    # اسم ملف JSON
    json_file = 'prices.json'
    
     # دالة داخلية لإضافة المنتج إلى ملف JSON
    def add_product_to_json():
        category = frame4_combobox.get()  # الحصول على اسم القسم من الكومبوبوكس
        product_name = frame4_entry1.get()  # الحصول على اسم المنتج من الإدخال
        product_price = frame4_entry2.get()  # الحصول على سعر المنتج من الإدخال

        # التحقق من أن كل الحقول غير فارغة
        if category and product_name and product_price:
            try:
                product_price = float(product_price)  # تحويل السعر إلى عدد
                add_product(json_file, category, product_name, product_price)  # إضافة المنتج
                CTkMessagebox(title="Success", message="تمت إضافة المنتج بنجاح", icon="check")
            except ValueError:
                CTkMessagebox(title="Error", message="الرجاء إدخال سعر صالح", icon="cancel")
        else:
            CTkMessagebox(title="Error", message="الرجاء ملء جميع الحقول", icon="cancel")


    frame4_btn1=CTkButton(master=frame4,text="اضافة",text_color="white",font=("Rubik",50),command=add_product_to_json)
    frame4_btn1.place(x=180,y=600)



# إنشاء متغير لحفظ السعر
price_var = tk.StringVar()

make_account()

root.mainloop()