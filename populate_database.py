#!/usr/bin/env python
"""
Database Population Script for BookHub
This script creates sample books and reviews with realistic data
"""

import os
import django
from datetime import date, timedelta
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Templates_Exercise.settings')
django.setup()

from books.models import Book
from reviews.models import Review


def clear_data():
    """Clear existing data from database"""
    print("🗑️  Clearing existing data...")
    Review.objects.all().delete()
    Book.objects.all().delete()
    print("✅ Data cleared successfully!")


def create_books():
    """Create sample books with realistic data"""
    print("\n📚 Creating books...")

    books_data = [
        # Fantasy Books
        {
            'title': 'The Name of the Wind',
            'author': 'Patrick Rothfuss',
            'genre': 'Fantasy',
            'price': Decimal('24.99'),
            'isbn': '978074345619',
            'publishing_date': date(2007, 3, 27),
            'description': 'A beautifully written epic fantasy novel about Kvothe, a legendary figure who recounts his life story. From his childhood in a troupe of traveling players to his years as a near-feral orphan in a crime-ridden city.',
            'image_url': 'https://images.unsplash.com/photo-1621351183012-e2f1f4e1a4a6?w=400&h=600&fit=crop',
            'slug': 'the-name-of-the-wind',
            'country': 'USA'
        },
        {
            'title': 'The Way of Kings',
            'author': 'Brandon Sanderson',
            'genre': 'Fantasy',
            'price': Decimal('29.99'),
            'isbn': '978076531756',
            'publishing_date': date(2010, 8, 31),
            'description': 'Epic fantasy at its finest. Roshar is a world of stone and storms. A world torn apart by hurricanes that blast through every few days is the focus of the war.',
            'image_url': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400&h=600&fit=crop',
            'slug': 'the-way-of-kings',
            'country': 'USA'
        },
        {
            'title': 'A Wizard of Earthsea',
            'author': 'Ursula K. Le Guin',
            'genre': 'Fantasy',
            'price': Decimal('18.99'),
            'isbn': '978055338304',
            'publishing_date': date(1968, 11, 1),
            'description': 'Ged was the greatest sorcerer in Earthsea, but in his youth he was the reckless Sparrowhawk. In his hunger for power and knowledge, he tampered with long-held secrets.',
            'image_url': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400&h=600&fit=crop',
            'slug': 'a-wizard-of-earthsea',
            'country': 'USA'
        },

        # Horror Books
        {
            'title': 'The Shining',
            'author': 'Stephen King',
            'genre': 'Horror',
            'price': Decimal('22.99'),
            'isbn': '978038512167',
            'publishing_date': date(1977, 1, 28),
            'description': 'Jack Torrance\'s new job at the Overlook Hotel is the perfect chance for a fresh start. But as the harsh winter weather sets in, the idyllic location feels ever more remote and sinister.',
            'image_url': 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=400&h=600&fit=crop',
            'slug': 'the-shining',
            'country': 'USA'
        },
        {
            'title': 'House of Leaves',
            'author': 'Mark Z. Danielewski',
            'genre': 'Horror',
            'price': Decimal('27.99'),
            'isbn': '978037570385',
            'publishing_date': date(2000, 3, 7),
            'description': 'A novel about a young family that moves into a small home on Ash Tree Lane where they discover something is terribly wrong: their house is bigger on the inside than it is on the outside.',
            'image_url': 'https://images.unsplash.com/photo-1509266272358-7701da638078?w=400&h=600&fit=crop',
            'slug': 'house-of-leaves',
            'country': 'USA'
        },
        {
            'title': 'Mexican Gothic',
            'author': 'Silvia Moreno-Garcia',
            'genre': 'Horror',
            'price': Decimal('21.99'),
            'isbn': '978052562017',
            'publishing_date': date(2020, 6, 30),
            'description': 'After receiving a frantic letter from her newly-wed cousin begging for someone to save her from a mysterious doom, socialite Noemí Taboada heads to High Place.',
            'image_url': 'https://images.unsplash.com/photo-1541963463532-d68292c34b19?w=400&h=600&fit=crop',
            'slug': 'mexican-gothic',
            'country': 'Mexico'
        },

        # Romance Books
        {
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'genre': 'Romance',
            'price': Decimal('14.99'),
            'isbn': '978014143951',
            'publishing_date': date(1813, 1, 28),
            'description': 'The romantic clash between the opinionated Elizabeth Bennet and the proud Mr. Darcy is a splendid performance of civilized sparring in one of the most famous novels.',
            'image_url': 'https://images.unsplash.com/photo-1524578271613-d550eacf6090?w=400&h=600&fit=crop',
            'slug': 'pride-and-prejudice',
            'country': 'UK'
        },
        {
            'title': 'The Notebook',
            'author': 'Nicholas Sparks',
            'genre': 'Romance',
            'price': Decimal('19.99'),
            'isbn': '978044652366',
            'publishing_date': date(1996, 10, 1),
            'description': 'Every so often a love story so captures our hearts that it becomes more than a story—it becomes an experience to remember forever.',
            'image_url': 'https://images.unsplash.com/photo-1516979187457-637abb4f9353?w=400&h=600&fit=crop',
            'slug': 'the-notebook',
            'country': 'USA'
        },
        {
            'title': 'Red, White & Royal Blue',
            'author': 'Casey McQuiston',
            'genre': 'Romance',
            'price': Decimal('23.99'),
            'isbn': '978125031646',
            'publishing_date': date(2019, 5, 14),
            'description': 'A big-hearted romantic comedy in which First Son Alex falls in love with Prince Henry of Wales after an incident of international proportions forces them to pretend to be best friends.',
            'image_url': 'https://images.unsplash.com/photo-1518133835878-5a93cc3f89e5?w=400&h=600&fit=crop',
            'slug': 'red-white-royal-blue',
            'country': 'USA'
        },

        # Thriller Books
        {
            'title': 'Gone Girl',
            'author': 'Gillian Flynn',
            'genre': 'Thriller',
            'price': Decimal('25.99'),
            'isbn': '978030758836',
            'publishing_date': date(2012, 6, 5),
            'description': 'On a warm summer morning in North Carthage, Missouri, it is Nick and Amy\'s fifth wedding anniversary. Amy disappears, and Nick becomes the prime suspect.',
            'image_url': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400&h=600&fit=crop',
            'slug': 'gone-girl',
            'country': 'USA'
        },
        {
            'title': 'The Girl with the Dragon Tattoo',
            'author': 'Stieg Larsson',
            'genre': 'Thriller',
            'price': Decimal('26.99'),
            'isbn': '978030745456',
            'publishing_date': date(2005, 8, 1),
            'description': 'Murder mystery, family saga, love story, and financial intrigue combine into one satisfyingly complex and entertainingly atmospheric novel.',
            'image_url': 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=400&h=600&fit=crop',
            'slug': 'the-girl-with-the-dragon-tattoo',
            'country': 'Sweden'
        },
        {
            'title': 'The Silent Patient',
            'author': 'Alex Michaelides',
            'genre': 'Thriller',
            'price': Decimal('24.99'),
            'isbn': '978125030170',
            'publishing_date': date(2019, 2, 5),
            'description': 'Alicia Berenson\'s life is seemingly perfect. One evening her husband Gabriel returns home late from work, and Alicia shoots him five times in the face, and then never speaks another word.',
            'image_url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400&h=600&fit=crop',
            'slug': 'the-silent-patient',
            'country': 'UK'
        },

        # Sci-Fi Books
        {
            'title': 'Dune',
            'author': 'Frank Herbert',
            'genre': 'Sci-Fi',
            'price': Decimal('28.99'),
            'isbn': '978044117271',
            'publishing_date': date(1965, 8, 1),
            'description': 'Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world where the only thing of value is the spice.',
            'image_url': 'https://images.unsplash.com/photo-1589998059171-988d887df646?w=400&h=600&fit=crop',
            'slug': 'dune',
            'country': 'USA'
        },
        {
            'title': 'Project Hail Mary',
            'author': 'Andy Weir',
            'genre': 'Sci-Fi',
            'price': Decimal('26.99'),
            'isbn': '978059313503',
            'publishing_date': date(2021, 5, 4),
            'description': 'Ryland Grace woke up on a spaceship with no idea why he\'s there. His crew is dead. All he knows is that he\'s been asleep for a long, long time.',
            'image_url': 'https://images.unsplash.com/photo-1614732414444-096e5f1122d5?w=400&h=600&fit=crop',
            'slug': 'project-hail-mary',
            'country': 'USA'
        },
        {
            'title': 'Neuromancer',
            'author': 'William Gibson',
            'genre': 'Sci-Fi',
            'price': Decimal('22.99'),
            'isbn': '978044100383',
            'publishing_date': date(1984, 7, 1),
            'description': 'The Matrix is a world within the world, a global consensus hallucination. Case had been the sharpest data-thief in the business, until a vengeful former employer crippled him.',
            'image_url': 'https://images.unsplash.com/photo-1555244162-803834f70033?w=400&h=600&fit=crop',
            'slug': 'neuromancer',
            'country': 'USA'
        },

        # Documentary/Non-Fiction Books
        {
            'title': 'Sapiens',
            'author': 'Yuval Noah Harari',
            'genre': 'Documentary',
            'price': Decimal('32.99'),
            'isbn': '978006231609',
            'publishing_date': date(2011, 9, 4),
            'description': 'How did our species succeed in the battle for dominance? Why did our foraging ancestors come together to create cities and kingdoms? How did we come to believe in gods?',
            'image_url': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=400&h=600&fit=crop',
            'slug': 'sapiens',
            'country': 'Israel'
        },
        {
            'title': 'Educated',
            'author': 'Tara Westover',
            'genre': 'Documentary',
            'price': Decimal('28.99'),
            'isbn': '978039959050',
            'publishing_date': date(2018, 2, 20),
            'description': 'A memoir about a young woman who, kept out of school, leaves her survivalist family and goes on to earn a PhD from Cambridge University.',
            'image_url': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=400&h=600&fit=crop',
            'slug': 'educated',
            'country': 'USA'
        },
        {
            'title': 'The Immortal Life of Henrietta Lacks',
            'author': 'Rebecca Skloot',
            'genre': 'Documentary',
            'price': Decimal('25.99'),
            'isbn': '978140023370',
            'publishing_date': date(2010, 2, 2),
            'description': 'Her name was Henrietta Lacks, but scientists know her as HeLa. She was a poor black tobacco farmer whose cells—taken without her knowledge—became one of the most important tools in medicine.',
            'image_url': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400&h=600&fit=crop',
            'slug': 'the-immortal-life-of-henrietta-lacks',
            'country': 'USA'
        },
    ]

    created_books = []
    for book_data in books_data:
        book = Book.objects.create(**book_data)
        created_books.append(book)
        print(f"  ✓ Created: {book.title} by {book.author}")

    print(f"✅ Successfully created {len(created_books)} books!")
    return created_books


def create_reviews(books):
    """Create sample reviews for books"""
    print("\n⭐ Creating reviews...")

    review_templates = [
        {
            'author': 'Sarah Johnson',
            'bodies': [
                'An absolute masterpiece! I couldn\'t put it down. The character development is phenomenal and the plot keeps you guessing until the very end.',
                'This book changed my perspective on the genre. The writing is beautiful and the story is incredibly moving.',
                'A thrilling read from start to finish. The author has crafted something truly special here.'
            ],
            'ratings': [Decimal('4.8'), Decimal('5.0'), Decimal('4.9')]
        },
        {
            'author': 'Michael Chen',
            'bodies': [
                'Gripping and intense. I found myself completely immersed in this world. Highly recommended!',
                'The pacing is perfect and the twists are unexpected. One of the best books I\'ve read this year.',
                'Compelling storytelling at its finest. The author knows how to keep readers engaged.'
            ],
            'ratings': [Decimal('4.7'), Decimal('4.9'), Decimal('4.6')]
        },
        {
            'author': 'Emily Rodriguez',
            'bodies': [
                'Beautiful prose and unforgettable characters. This book will stay with me for a long time.',
                'A powerful and emotional journey. I laughed, I cried, and I was completely captivated.',
                'Excellent read! The world-building is incredible and the plot is expertly crafted.'
            ],
            'ratings': [Decimal('5.0'), Decimal('4.8'), Decimal('4.9')]
        },
        {
            'author': 'David Thompson',
            'bodies': [
                'Fascinating and thought-provoking. This book challenges you to think differently.',
                'Well-written and engaging throughout. The author has a unique voice that really shines.',
                'A solid read with great character arcs and an interesting premise.'
            ],
            'ratings': [Decimal('4.5'), Decimal('4.6'), Decimal('4.4')]
        },
        {
            'author': 'Jessica Martinez',
            'bodies': [
                'Absolutely loved it! The story is both heartwarming and heartbreaking in the best way.',
                'Incredible storytelling. The author weaves together multiple storylines seamlessly.',
                'A must-read! This book exceeded all my expectations and more.'
            ],
            'ratings': [Decimal('4.9'), Decimal('5.0'), Decimal('4.8')]
        },
        {
            'author': 'Robert Williams',
            'bodies': [
                'Great book with well-developed characters and an engaging plot. Definitely worth reading.',
                'The author has created something truly special. The attention to detail is remarkable.',
                'An enjoyable read with plenty of twists and turns to keep you engaged.'
            ],
            'ratings': [Decimal('4.3'), Decimal('4.7'), Decimal('4.5')]
        },
        {
            'author': 'Amanda Lee',
            'bodies': [
                'Stunning and beautifully written. Every page is a treasure.',
                'This book hooked me from the first chapter. The storytelling is masterful.',
                'A fantastic addition to the genre. I highly recommend it to anyone looking for a great read.'
            ],
            'ratings': [Decimal('4.8'), Decimal('4.9'), Decimal('4.7')]
        },
        {
            'author': 'Christopher Brown',
            'bodies': [
                'Intense and captivating. The author knows how to build tension and keep readers on edge.',
                'One of the best books I\'ve read in years. The plot is intricate and satisfying.',
                'Excellent work! The characters feel real and the story is compelling.'
            ],
            'ratings': [Decimal('4.6'), Decimal('4.8'), Decimal('4.5')]
        },
    ]

    reviews_created = 0
    for book in books:
        # Create 2-4 reviews per book
        import random
        num_reviews = random.randint(2, 4)

        for i in range(num_reviews):
            template = review_templates[i % len(review_templates)]
            body_index = random.randint(0, len(template['bodies']) - 1)

            review = Review.objects.create(
                author=template['author'],
                body=template['bodies'][body_index],
                rating=template['ratings'][body_index],
                book=book
            )
            reviews_created += 1

    print(f"✅ Successfully created {reviews_created} reviews!")


def main():
    """Main function to populate the database"""
    print("=" * 60)
    print("📖 BookHub Database Population Script")
    print("=" * 60)

    # Clear existing data
    clear_data()

    # Create books
    books = create_books()

    # Create reviews
    create_reviews(books)

    print("\n" + "=" * 60)
    print("🎉 Database population completed successfully!")
    print("=" * 60)
    print(f"\nSummary:")
    print(f"  📚 Total Books: {Book.objects.count()}")
    print(f"  ⭐ Total Reviews: {Review.objects.count()}")
    print(f"\nYou can now run the Django server and view the data!")
    print("=" * 60)


if __name__ == '__main__':
    main()
