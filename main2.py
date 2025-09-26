import customtkinter as ctk
from tkinter import messagebox
from database import Database
from downloader import Downloader
import threading
from pathlib import Path

# Set theme and color
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginWindow:
    def __init__(self):
        self.db = Database()
        
        # Crear la ventana principal
        self.root = ctk.CTk()
        self.root.title("Login - Clip2Sound")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        
        # Centrar la ventana
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 450) // 2
        self.root.geometry(f"400x450+{x}+{y}")
        
        self.create_login_frame()
        
    def create_login_frame(self):
        # Main frame
        self.login_frame = ctk.CTkFrame(self.root)
        self.login_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Titulo
        title_label = ctk.CTkLabel(
            self.login_frame, 
            text="Clip2Sound",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=30)
        
        # Usuario
        self.username_entry = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Usuario",
            width=250,
            height=40
        )
        self.username_entry.pack(pady=10)
        
        # Contraseña
        self.password_entry = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Contraseña",
            show="●",
            width=250,
            height=40
        )
        self.password_entry.pack(pady=10)
        
        # Boton Login
        login_button = ctk.CTkButton(
            self.login_frame,
            text="Login",
            command=self.login,
            width=250,
            height=40
        )
        login_button.pack(pady=10)
        
        # Boton Registrarse
        register_button = ctk.CTkButton(
            self.login_frame,
            text="Registrarse",
            command=self.register,
            width=250,
            height=40,
            fg_color="transparent",
            border_width=2
        )
        register_button.pack(pady=10)
    
    # Logica Login
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        user_id = self.db.verify_user(username, password)
        if user_id:
            self.root.withdraw()
            app = MainWindow(user_id, username, self)
        else:
            messagebox.showerror("Error", "Usuario o Contraseña invalida.")
    
    # Logica Registrarse
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor llene todos los espacios.")
            return
        
        if len(username) <= 3:
            messagebox.showerror("Error", "El usuario debe de ser de mas de 3 caracteres.")
            return
        
        elif len(password) <= 5:
            messagebox.showerror("Error", "La contraseña debe de ser de mas de 5 caracteres.")
            return
        
        if self.db.add_user(username, password):
            messagebox.showinfo("Registro Exitoso", "Usuario resgistrado con exito.")
        else:
            messagebox.showerror("Error", "El usuario ya existe.")
    
    def show(self):
        self.root.deiconify()
        self.username_entry.delete(0, ctk.END)
        self.password_entry.delete(0, ctk.END)
    
    def run(self):
        self.root.mainloop()

# Ventana Principal
class MainWindow:
    def __init__(self, user_id, username, login_window):
        self.db = Database()
        self.current_user = user_id
        self.login_window = login_window
        
        self.root = ctk.CTkToplevel()
        self.root.title(f"Clip2Sound - {username}")
        self.root.geometry("900x700")
        
        # Centrar ventana
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 900) // 2
        y = (screen_height - 700) // 2
        self.root.geometry(f"900x700+{x}+{y}")
        
        # Cerrar ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.create_main_frame()
        
        # Downloader
        download_path = self.db.get_download_path(user_id)
        if not download_path:
            download_path = str(Path.home() / "Downloads")
            self.db.update_download_path(user_id, download_path)
        self.downloader = Downloader(download_path)
    
    def create_main_frame(self):
        # Main container
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # URL entry frame
        url_frame = ctk.CTkFrame(self.main_frame)
        url_frame.pack(fill='x', pady=10)
        
        url_label = ctk.CTkLabel(url_frame, text="YouTube URL:")
        url_label.pack(side='left', padx=10)
        
        self.url_entry = ctk.CTkEntry(url_frame, placeholder_text="Ingrese URL del video", height=35)
        self.url_entry.pack(side='left', fill='x', expand=True, padx=10)
        
        # Buttons frame
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(fill='x', pady=20)
        
        # Download buttons
        ctk.CTkButton(
            button_frame,
            text="Descargar Single",
            command=lambda: self.start_download(False),
            width=150,
            height=35
        ).pack(side='left', padx=5)
        
        ctk.CTkButton(
            button_frame,
            text="Descargar Playlist",
            command=lambda: self.start_download(True),
            width=150,
            height=35
        ).pack(side='left', padx=5)
        
        ctk.CTkButton(
            button_frame,
            text="Seleccionar Folder",
            command=self.select_folder,
            width=150,
            height=35
        ).pack(side='left', padx=5)
        
        ctk.CTkButton(
            button_frame,
            text="Logout",
            command=self.logout,
            width=100,
            height=35,
            fg_color="transparent",
            border_width=2
        ).pack(side='right', padx=5)
        
        # Download history frame
        history_frame = ctk.CTkFrame(self.main_frame)
        history_frame.pack(fill='both', expand=True, pady=10)
        
        history_label = ctk.CTkLabel(
            history_frame,
            text="Historial de descargas:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        history_label.pack(anchor='w', padx=10, pady=10)
        
        # Create treeview with custom styling
        self.history_tree = ctk.CTkTextbox(history_frame)
        self.history_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Progress label
        self.progress_var = ctk.StringVar(value="Completado")
        progress_label = ctk.CTkLabel(
            self.main_frame,
            textvariable=self.progress_var,
            font=ctk.CTkFont(size=14)
        )
        progress_label.pack(pady=10)
        
        self.update_history()
    
    def select_folder(self):
        folder = ctk.filedialog.askdirectory()
        if folder:
            self.db.update_download_path(self.current_user, folder)
            self.downloader.download_path = folder
            messagebox.showinfo("Exito", "Se selecciono el folder.")
    
    def start_download(self, is_playlist):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Por favor ingrese la url.")
            return
        
        self.progress_var.set("Descargando...")
        
        def download_thread():
            try:
                if is_playlist:
                    results = self.downloader.download_playlist(url)
                    for result in results:
                        if result['success']:
                            self.db.add_download(
                                self.current_user,
                                result['video_id'],
                                result['title']
                            )
                else:
                    result = self.downloader.download_video(url)
                    if result['success']:
                        self.db.add_download(
                            self.current_user,
                            result['video_id'],
                            result['title']
                        )
                
                self.root.after(0, lambda: self.progress_var.set("Descarga completa."))
                self.root.after(0, self.update_history)
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
                self.root.after(0, lambda: self.progress_var.set("Error"))
        
        thread = threading.Thread(target=download_thread)
        thread.daemon = True
        thread.start()
    
    def update_history(self):
        self.history_tree.delete('1.0', ctk.END)
        downloads = self.db.get_user_downloads(self.current_user)
        
        if not downloads:
            self.history_tree.insert('1.0', "No hay descargas registradas.")
            return
            
        for title, date in downloads:
            self.history_tree.insert(ctk.END, f"Título: {title}\nFecha: {date}\n\n")
    
    def logout(self):
        self.root.destroy()
        self.login_window.show()
    
    def on_closing(self):
        self.root.destroy()
        self.login_window.root.destroy()

if __name__ == "__main__":
    login = LoginWindow()
    login.run()