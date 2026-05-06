class Book:
    def __init__(self,name,author):
       self.name=name
       self.author=author
       self.reviews=[]
    def add_review(self,review):
        self.reviews.append(review)
    def count_reviews(self):
        print(len(self.reviews)) 
    def display_reviews(self):
        for review in self.reviews:
            print(review)
book1=Book("Hary Potter", "J.K.Rowling")
book1.add_review("Super book")
book1.add_review("Excellent book")
book1.count_reviews()
book1.display_reviews()       
