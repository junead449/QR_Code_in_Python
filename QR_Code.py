import qrcode as qr
#Enter the Link that you want to create the Qr of that account etc.
img=qr.make("https://www.coursera.org/programs/dlsei-phase-2-52jvh?currentTab=CATALOG")
#Enter the name and file type of that qr
img.save("Chaudhary Junead.png")
