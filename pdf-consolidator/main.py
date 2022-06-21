from dis import show_code
import glob
import fitz

def getFiles():
    output = fitz.open()
    for i in glob.glob('input/*.pdf'):
        doc = fitz.open(i)
        output.insert_pdf(doc, show_progress=1)
    output.save('output.pdf')
    output.close()

if __name__ == "__main__":
    print("hi")
    getFiles()