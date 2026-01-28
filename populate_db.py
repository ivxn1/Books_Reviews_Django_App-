"""
Script to populate the database with sample books and reviews.
Run this script from the project root directory: python populate_db.py
"""

import os
import sys
import django
from datetime import date, datetime
from decimal import Decimal

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Templates_Exercise.settings')
django.setup()

from books.models import Book
from reviews.models import Review


def create_books():
    """Create sample book entries"""
    books_data = [
        {
            'title': 'The Hobbit',
            'author': 'J.R.R. Tolkien',
            'price': Decimal('15.99'),
            'isbn': '978054792822',
            'genre': 'Fantasy',
            'publishing_date': date(1937, 9, 21),
            'description': 'A fantasy novel about Bilbo Baggins, a hobbit who embarks on an unexpected adventure with a group of dwarves and the wizard Gandalf.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/71V2v2GtAtL.jpg',
            'slug': 'the-hobbit',
            'country': 'United Kingdom'
        },
        {
            'title': 'Dune',
            'author': 'Frank Herbert',
            'price': Decimal('18.99'),
            'isbn': '978044172641',
            'genre': 'Sci-Fi',
            'publishing_date': date(1965, 8, 1),
            'description': 'A science fiction novel set in the distant future amidst a sprawling feudal interstellar society, telling the story of young Paul Atreides.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/81ym3zu0HmL.jpg',
            'slug': 'dune',
            'country': 'United States'
        },
        {
            'title': 'The Shining',
            'author': 'Stephen King',
            'price': Decimal('14.99'),
            'isbn': '978038512167',
            'genre': 'Horror',
            'publishing_date': date(1977, 1, 28),
            'description': 'A horror novel about Jack Torrance, who becomes winter caretaker at the isolated Overlook Hotel, where he descends into madness.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/91U8l6FdOYL.jpg',
            'slug': 'the-shining',
            'country': 'United States'
        },
        {
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'price': Decimal('12.99'),
            'isbn': '978014143951',
            'genre': 'Romance',
            'publishing_date': date(1813, 1, 28),
            'description': 'A romantic novel following Elizabeth Bennet as she deals with issues of manners, upbringing, morality, and marriage in society.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/71Q1tPupKjL.jpg',
            'slug': 'pride-and-prejudice',
            'country': 'United Kingdom'
        },
        {
            'title': 'Gone Girl',
            'author': 'Gillian Flynn',
            'price': Decimal('16.99'),
            'isbn': '978030758836',
            'genre': 'Thriller',
            'publishing_date': date(2012, 6, 5),
            'description': 'A psychological thriller about a woman who goes missing on her fifth wedding anniversary, and her husband becomes the prime suspect.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/71awjh2FmOL.jpg',
            'slug': 'gone-girl',
            'country': 'United States'
        },
        {
            'title': 'The Lord of the Rings',
            'author': 'J.R.R. Tolkien',
            'price': Decimal('24.99'),
            'isbn': '978054792819',
            'genre': 'Fantasy',
            'publishing_date': date(1954, 7, 29),
            'description': 'An epic high fantasy novel following the quest to destroy the One Ring and defeat the Dark Lord Sauron.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/91jBdze-l8L.jpg',
            'slug': 'the-lord-of-the-rings',
            'country': 'United Kingdom'
        },
        {
            'title': 'Sapiens: A Brief History of Humankind',
            'author': 'Yuval Noah Harari',
            'price': Decimal('19.99'),
            'isbn': '978006231609',
            'genre': 'Documentary',
            'publishing_date': date(2011, 1, 1),
            'description': 'A book exploring the history of humankind from the Stone Age to the modern age, driven by unique cognitive abilities.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/713jIoMO3UL.jpg',
            'slug': 'sapiens',
            'country': 'Israel'
        },
        {
            'title': 'It',
            'author': 'Stephen King',
            'price': Decimal('17.99'),
            'isbn': '978045141439',
            'genre': 'Horror',
            'publishing_date': date(1986, 9, 15),
            'description': 'A horror novel about seven children who are terrorized by a being that exploits the fears and phobias of its victims.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/71nRbCOFKUL.jpg',
            'slug': 'it',
            'country': 'United States'
        },
        {
            'title': 'The Girl on the Train',
            'author': 'Paula Hawkins',
            'price': Decimal('15.49'),
            'isbn': '978159463402',
            'genre': 'Thriller',
            'publishing_date': date(2015, 1, 13),
            'description': 'A psychological thriller about a divorcee who becomes entangled in a missing person investigation.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/91VUWXhN4eL.jpg',
            'slug': 'the-girl-on-the-train',
            'country': 'United Kingdom'
        },
        {
            'title': 'Foundation',
            'author': 'Isaac Asimov',
            'price': Decimal('16.49'),
            'isbn': '978055329335',
            'genre': 'Sci-Fi',
            'publishing_date': date(1951, 6, 1),
            'description': 'A science fiction novel about mathematician Hari Seldon who develops psychohistory to predict the future of large populations.',
            'image_url': 'https://images-na.ssl-images-amazon.com/images/I/81JNIo9s-tL.jpg',
            'slug': 'foundation',
            'country': 'United States'
        }
    ]

    created_books = []
    for book_data in books_data:
        book, created = Book.objects.get_or_create(
            isbn=book_data['isbn'],
            defaults=book_data
        )
        if created:
            print(f"✓ Created book: {book.title}")
        else:
            print(f"- Book already exists: {book.title}")
        created_books.append(book)

    return created_books


def create_reviews(books):
    """Create sample review entries for the books"""
    reviews_data = [
        # Reviews for The Hobbit
        {
            'author': 'Sarah Johnson',
            'body': 'An absolute masterpiece! The world-building is incredible and the adventure is captivating from start to finish. A must-read for any fantasy lover.',
            'rating': Decimal('4.8'),
            'book': books[0]
        },
        {
            'author': 'Michael Chen',
            'body': 'A charming tale that appeals to both children and adults. Tolkien\'s writing style is engaging and the characters are memorable.',
            'rating': Decimal('4.6'),
            'book': books[0]
        },
        {
            'author': 'Emma Wilson',
            'body': 'The perfect introduction to Middle-earth. Bilbo\'s journey is inspiring and full of wonderful moments.',
            'rating': Decimal('4.9'),
            'book': books[0]
        },
        # Reviews for Dune
        {
            'author': 'David Martinez',
            'body': 'A complex and brilliant sci-fi epic. The political intrigue and world-building are unmatched. Takes time to get into but worth it.',
            'rating': Decimal('4.7'),
            'book': books[1]
        },
        {
            'author': 'Lisa Anderson',
            'body': 'Dense but rewarding. Herbert creates a fully realized universe with deep philosophical themes. A true science fiction classic.',
            'rating': Decimal('4.5'),
            'book': books[1]
        },
        # Reviews for The Shining
        {
            'author': 'James Taylor',
            'body': 'Terrifying and atmospheric. King is a master of psychological horror. This book kept me up at night!',
            'rating': Decimal('4.7'),
            'book': books[2]
        },
        {
            'author': 'Rebecca Moore',
            'body': 'Genuinely scary and deeply psychological. The descent into madness is portrayed brilliantly. Much better than the movie.',
            'rating': Decimal('4.8'),
            'book': books[2]
        },
        {
            'author': 'Tom Harris',
            'body': 'A horror masterpiece that explores themes of addiction and family. Incredibly suspenseful.',
            'rating': Decimal('4.6'),
            'book': books[2]
        },
        # Reviews for Pride and Prejudice
        {
            'author': 'Grace Thompson',
            'body': 'A timeless romance with sharp wit and social commentary. Elizabeth Bennet is one of literature\'s greatest heroines.',
            'rating': Decimal('4.9'),
            'book': books[3]
        },
        {
            'author': 'Oliver Brown',
            'body': 'Austen\'s prose is delightful and the romance between Elizabeth and Darcy is perfectly developed. A true classic.',
            'rating': Decimal('4.8'),
            'book': books[3]
        },
        # Reviews for Gone Girl
        {
            'author': 'Amanda White',
            'body': 'A twisted psychological thriller that keeps you guessing until the very end. The unreliable narrators are brilliantly written.',
            'rating': Decimal('4.5'),
            'book': books[4]
        },
        {
            'author': 'Ryan Clark',
            'body': 'Dark, clever, and completely unpredictable. Flynn crafts a story that will mess with your mind. Highly entertaining.',
            'rating': Decimal('4.4'),
            'book': books[4]
        },
        {
            'author': 'Jennifer Lee',
            'body': 'A page-turner with plenty of twists. The characters are complex and morally ambiguous. Couldn\'t put it down.',
            'rating': Decimal('4.6'),
            'book': books[4]
        },
        # Reviews for The Lord of the Rings
        {
            'author': 'Christopher Young',
            'body': 'The greatest fantasy epic ever written. Tolkien\'s world is so detailed and immersive. A journey worth taking multiple times.',
            'rating': Decimal('5.0'),
            'book': books[5]
        },
        {
            'author': 'Sophia King',
            'body': 'An epic adventure with unforgettable characters and themes. The descriptions can be lengthy but the story is incredible.',
            'rating': Decimal('4.8'),
            'book': books[5]
        },
        # Reviews for Sapiens
        {
            'author': 'Daniel Roberts',
            'body': 'Mind-blowing and thought-provoking. Harari presents human history in a fascinating and accessible way. Changed my perspective on humanity.',
            'rating': Decimal('4.7'),
            'book': books[6]
        },
        {
            'author': 'Victoria Green',
            'body': 'An engaging overview of human history that challenges conventional thinking. Some controversial points but overall excellent.',
            'rating': Decimal('4.5'),
            'book': books[6]
        },
        # Reviews for It
        {
            'author': 'Matthew Scott',
            'body': 'Terrifying and emotionally powerful. King\'s best work in my opinion. The childhood friendship dynamics are as important as the horror.',
            'rating': Decimal('4.9'),
            'book': books[7]
        },
        {
            'author': 'Hannah Davis',
            'body': 'A massive book but gripping throughout. Pennywise is one of the most terrifying villains in literature. The coming-of-age story is beautiful.',
            'rating': Decimal('4.7'),
            'book': books[7]
        },
        # Reviews for The Girl on the Train
        {
            'author': 'Nathan Miller',
            'body': 'A fast-paced thriller with unreliable narrators. Kept me hooked from beginning to end. Great for fans of psychological mysteries.',
            'rating': Decimal('4.3'),
            'book': books[8]
        },
        {
            'author': 'Olivia Turner',
            'body': 'Suspenseful and engaging. The multiple perspectives add depth to the mystery. A real page-turner.',
            'rating': Decimal('4.4'),
            'book': books[8]
        },
        # Reviews for Foundation
        {
            'author': 'Ethan Phillips',
            'body': 'A brilliant exploration of empire, knowledge, and prediction. Asimov\'s vision of the future is fascinating and thought-provoking.',
            'rating': Decimal('4.6'),
            'book': books[9]
        },
        {
            'author': 'Isabella Martinez',
            'body': 'Classic science fiction at its best. The concept of psychohistory is fascinating. A must-read for any sci-fi fan.',
            'rating': Decimal('4.7'),
            'book': books[9]
        }
    ]

    created_count = 0
    for review_data in reviews_data:
        review, created = Review.objects.get_or_create(
            author=review_data['author'],
            book=review_data['book'],
            defaults={
                'body': review_data['body'],
                'rating': review_data['rating']
            }
        )
        if created:
            print(f"✓ Created review by {review.author} for {review.book.title}")
            created_count += 1
        else:
            print(f"- Review already exists: {review.author} for {review.book.title}")

    return created_count


def main():
    """Main function to populate the database"""
    print("=" * 60)
    print("Starting database population...")
    print("=" * 60)
    print()

    print("Creating books...")
    print("-" * 60)
    books = create_books()
    print()

    print("Creating reviews...")
    print("-" * 60)
    reviews_count = create_reviews(books)
    print()

    print("=" * 60)
    print(f"Database population complete!")
    print(f"Total books in database: {Book.objects.count()}")
    print(f"Total reviews in database: {Review.objects.count()}")
    print("=" * 60)


if __name__ == '__main__':
    main()
