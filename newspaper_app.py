"""
    Author: Aritra Bhattacharjee
    Date of Working: 21.04.2022 to 22.04.2022
    Tech Stack: Python, Tkinter.
    About: A python based GUI application that shows news according to various categories.
"""
import tkinter
import requests
import apikey # this is a custom file that contains my apikey
types = 'sports'
BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={types}&apiKey={apikey.api_key}'

# apikey = "Your Api Key"
# BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={types}&apiKey={apikey}'

# defining a NewsApp class
class NewsApp:
    global api_key,types

    
    def __init__(self,root):
        self.root = root
        self.root.geometry('1370x700')
        self.root.title("News Viewer")

        tkinter.Label(self.root,text="NewsPaper App",font=("times new roman",30,"bold"),pady=2,bd=12,relief=tkinter.GROOVE).pack(fill=tkinter.X)
        
        self.newsCategory = ["general","sports","business","technology","health"]

        labelframe = tkinter.LabelFrame(self.root,text="Category",font=('times new roman',20,'bold'),bd = 10,relief=tkinter.GROOVE)
        labelframe.place(x=10,y=80,width=300,relheight=0.80)

        self.newsCategoryButton = []

        for i in range(len(self.newsCategory)):
            btn = tkinter.Button(labelframe,text = self.newsCategory[i].upper(),font=('arial',15,'bold'),width=20,bd=7)
            btn.grid(row = i,column=0,padx=10,pady =5)
            btn.bind('<Button-1>',self.News)
            self.newsCategoryButton.append(btn)

        #  News Frame 
        newsFrame = tkinter.Frame(self.root,bd=7,relief=tkinter.GROOVE)
        newsFrame.place(x=320,y=80,relheight=0.8,relwidth=0.7)
        tkinter.Label(newsFrame,text = "News",bd= 5,font = ('arial',20,'bold'),relief=tkinter.GROOVE).pack(fill=tkinter.X)

        scrollbar  = tkinter.Scrollbar(newsFrame,orient=tkinter.VERTICAL)
        self.textarea = tkinter.Text(newsFrame,yscrollcommand=scrollbar.set,font=("times new roman",15,"bold"))
        scrollbar.pack(side=tkinter.RIGHT,fill =tkinter.Y)
        scrollbar.config(command=self.textarea.yview)
        self.textarea.insert(tkinter.END,"Please select your desired category to get corresponding news! ")
        self.textarea.pack(fill=tkinter.BOTH,expand=1)


    def News(self,event):
        
        category = event.widget.cget('text').lower()
        BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={apikey.api_key}'
        self.textarea.delete("1.0",tkinter.END)        
        self.textarea.insert(tkinter.END,f"\n Welcome to {category.upper()} News\n")
        self.textarea.insert(tkinter.END,"------------------------------------------------------------------------------------------------------------------\n")
        try:
            articles = (requests.get(BASE_URL).json())['articles']
            if articles!=0:
                for i in range(len(articles)):
                    self.textarea.insert(tkinter.END,f"{articles[i]['title']}\n")
                    self.textarea.insert(tkinter.END,f"{articles[i]['description']}\n\n")

                    self.textarea.insert(tkinter.END,f"To Read more details, follow the link : {articles[i]['url']}\n")

                    self.textarea.insert(tkinter.END,"------------------------------------------------------------------------------------------------------------------\n")
                    self.textarea.insert(tkinter.END,"------------------------------------------------------------------------------------------------------------------\n")
                else:
                    self.textarea.insert(tkinter.END,"Sorry, no news available")
        except Exception as e:
            tkinter.messagebox.showerror('ERROR',"Sorry, can't connect")


if __name__ == '__main__':
    root = tkinter.Tk()
    obj = NewsApp(root)
    root.mainloop()
