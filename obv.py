import tkinter as a,b from tkinter import messagebox as c,ttk as d, filedialog as e;import psutil as f,os,threading as g,time;from datetime import datetime as h,timedelta as i;import matplotlib.pyplot as j;from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as k;from ttkthemes import ThemedTk as l;X,Y,Z=1000,3600,None;L,M,N=[], "parentpass","childpass";G,hZ={}, h.now();B,C,D,E,F,G="⚙️","⚡","🔒","🎮","🛡️","✅";A=l(theme="equilux");A.title("Smart Energy Manager 💻");A.geometry("1000x600");A.resizable(False,False)
def H():global X,Y,hZ;hZ=h.now();X,Y=1000,3600;c.showinfo("Reset",f"{C} Limits have been reset for the new day! {C}")
def I():global Z,L,hZ;Z=time.time()
    while L:
        s=time.time()-Z;E=f.cpu_percent(interval=1);t=E*10
        if t>X or s>Y:K();break
        if h.now()>=hZ+i(days=1):H();time.sleep(1)
def K():c.showwarning("Warning",f"{E} Energy or Time limit exceeded! Closing apps.");[os.system(f"taskkill /f /im {v}")for v in G.values()]
def J(p):u,jx=p.subplots(figsize=(5,3));jx.set_title("Energy Consumption Over Time");jx.set_xlabel("Time (s)");jx.set_ylabel("Energy (Watts)");t=[0]
    def tY():
        if L:
            E=f.cpu_percent(interval=1);s=E*10;t.append(s)
            if len(t)>10:t.pop(0)
            jx.clear();jx.plot(t,color='blue');jx.set_title("Energy Consumption Over Time");jx.set_xlabel("Time (s)");jx.set_ylabel("Energy (Watts)");v.draw()
        p.after(1000,tY)
    v=k(u,master=p);v.draw();v.get_tk_widget().pack(side=b.TOP,fill=b.BOTH,expand=True);p.after(1000,tY)
def w():q=b.Toplevel(A);q.title(f"Settings {F}");q.geometry("400x400");b.Label(q,text="Settings Menu",font=("Helvetica",16)).pack(pady=20);b.Label(q,text="Change Parent Password:").pack(pady=10);r=b.Entry(q,show='*');r.pack(pady=5)
    def x():global M;M=r.get();c.showinfo("Success",f"{F} Parent password updated!")
    b.Button(q,text="Update Password",command=x).pack(pady=10)
def y(P):z=b.Toplevel(A);z.title(f"{P.capitalize()} Login {E}");z.geometry("400x250");b.Label(z,text="Enter Username").grid(row=0,column=0,padx=10,pady=10);b.Label(z,text="Enter Password").grid(row=1,column=0,padx=10,pady=10);a=b.Entry(z);b_=b.Entry(z,show='*');a.grid(row=0,column=1,padx=10,pady=10);b_.grid(row=1,column=1,padx=10,pady=10)
    def iI():
        if P=="parent" and a.get()=="parent" and b_.get()==M:c.showinfo("Success",f"{G} Parent Login Successful!");z.destroy();pO()
        elif P=="child" and a.get()=="child" and b_.get()==N:c.showinfo("Success",f"{G} Child Login Successful!");z.destroy();qA()
        else:c.showerror("Error",f"{E} Invalid Credentials!")
    b.Button(z,text=f"Login {E}",command=iI).grid(row=2,column=1,pady=10)
def pO():a=b.Toplevel(A);a.title(f"Parent Dashboard {F}");a.geometry("800x500");b.Label(a,text="Energy Limit (W)").grid(row=0,column=0,padx=10,pady=10);c=b.Entry(a);c.grid(row=0,column=1,padx=10,pady=10);c.insert(0,str(X));b.Label(a,text="Time Limit (Minutes)").grid(row=1,column=0,padx=10,pady=10);d=b.Entry(a);d.grid(row=1,column=1,padx=10,pady=10);d.insert(0,str(int(Y/60)))
    def z():global X,Y;X=int(c.get());Y=int(d.get())*60;c.showinfo("Success",f"{G} Limits Updated!")
    b.Button(a,text="Update Limits",command=z).grid(row=2,column=1,pady=10);s=b.Frame(a,width=400,height=300);s.grid(row=3,column=0,columnspan=2,pady=20);J(s)
def qA():x=b.Toplevel(A);x.title(f"Child Interface {D}");x.geometry("400x300");b.Label(x,text="Enter Game/App to Request:").grid(row=0,column=0,padx=10,pady=10);y=b.Entry(x);y.grid(row=1,column=0,padx=10,pady=10)
    def p():z=y.get()
        if z:L.append(z);c.showinfo("Request Sent",f"{B} Request for {z} sent to parent.")
    b.Button(x,text="Request Access",command=p).grid(row=2,column=0,pady=10)
def q():global L,hZ;L=True;hZ=h.now();A=g.Thread(target=I);A.start()
def r():global L;L=False;c.showinfo("Tracking Stopped",f"{E} Energy tracking has been stopped.")
b.Button(A,text=f"Settings {B}",command=w).place(relx=0.9,rely=0.05);b.Button(A,text=f"Login {D}",command=lambda:y("parent")).place(relx=0.45,rely=0.5);A.mainloop()
