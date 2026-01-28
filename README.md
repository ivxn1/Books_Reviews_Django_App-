# 📚 BookHub - Django Templates Exercise

A beautiful, modern Django web application for browsing and reviewing books with stunning HTML/CSS layouts.

## 🎨 Features

### Beautiful Modern Design
- **Responsive Layout**: Fully responsive design that works on desktop, tablet, and mobile
- **Gradient Color Schemes**: Modern gradient backgrounds using purple and blue tones
- **Smooth Animations**: Fade-in animations and hover effects for enhanced user experience
- **Card-Based Layout**: Clean card designs for displaying books
- **Professional Typography**: Modern font stack with proper hierarchy

### Template Structure
- ✅ **base.html** - Main template with CSS variables, utility classes, and base layout
- ✅ **_header.html** - Sticky header with gradient background and navigation
- ✅ **_footer.html** - Multi-column footer with links and social media
- ✅ **index.html** - Beautiful home page with hero section, features, and stats
- ✅ **book_list.html** - Book listing page with filters and card grid

### Database
- 📚 **18 Books** across 6 genres (Fantasy, Horror, Romance, Thriller, Sci-Fi, Documentary)
- ⭐ **54 Reviews** with realistic ratings and content
- 🖼️ **Book Images** using Unsplash URLs

## 📁 Project Structure

```
Templates_Exercise/
├── manage.py
├── populate_database.py          # Script to populate DB with sample data
├── books/                         # Books app
│   ├── models.py                 # Book model
│   ├── views.py                  # Book views
│   └── urls.py
├── reviews/                       # Reviews app
│   └── models.py                 # Review model
├── templates/
│   ├── core/
│   │   ├── base.html            # Main base template
│   │   └── partials/
│   │       ├── _header.html     # Header partial
│   │       └── _footer.html     # Footer partial
│   ├── index.html               # Home page
│   └── book_list.html           # Book listing page
└── Templates_Exercise/
    └── settings.py
```

## 🚀 Quick Start

### 1. Populate the Database

Run the database population script to create sample books and reviews:

```bash
python populate_database.py
```

This will create:
- 18 books across different genres
- 54 reviews from various authors
- Realistic data including titles, descriptions, prices, ISBNs, and images

### 2. Run the Server

```bash
python manage.py runserver
```

### 3. View the Site

Open your browser and navigate to:
- **Home Page**: http://127.0.0.1:8000/
- **Book List**: http://127.0.0.1:8000/books/

## 🎨 Design Features

### Color Palette
```css
--primary-color: #2563eb      /* Blue */
--primary-dark: #1e40af       /* Dark Blue */
--secondary-color: #8b5cf6    /* Purple */
--text-dark: #1f2937          /* Dark Gray */
--text-light: #6b7280         /* Light Gray */
--bg-light: #f9fafb           /* Light Background */
```

### Gradient Themes
- **Header/Footer**: Purple to violet gradient (667eea → 764ba2)
- **Genre Badges**: Unique colors for each genre
  - Fantasy: Purple (#8b5cf6)
  - Horror: Red (#ef4444)
  - Romance: Pink (#ec4899)
  - Thriller: Orange (#f59e0b)
  - Sci-Fi: Green (#10b981)
  - Documentary: Blue (#6366f1)

### Components

#### Header
- Sticky navigation with gradient background
- Search box with blur effect
- Hover animations on navigation links
- Fully responsive mobile menu

#### Footer
- 4-column grid layout
- Social media links
- Quick links and category links
- Gradient background matching header

#### Book Cards
- Image with overlay genre badge
- Title, description, and price
- Publishing date
- Hover effect with lift animation
- Action buttons (View Details, Add to Cart)

#### Filter Section
- Genre filter dropdown
- Sort options (price, title, date)
- Search input
- Apply filters button

## 📝 Template Features

### No Django Filters Used
All templates are created **WITHOUT Django template filters** so you can practice adding them later. The templates use:
- Basic variable rendering: `{{ variable }}`
- Template inheritance: `{% extends %}`
- Template includes: `{% include %}`
- Basic loops: `{% for %}`
- Conditionals: `{% if %}`

### Ready for Filters Practice
You can now practice adding Django filters like:
- `{{ book.price|floatformat:2 }}`
- `{{ book.title|upper }}`
- `{{ book.description|truncatewords:20 }}`
- `{{ book.publishing_date|date:"F j, Y" }}`
- `{{ book.genre|lower }}`

## 🎯 Sample Books Included

### Fantasy (3 books)
- The Name of the Wind - Patrick Rothfuss
- The Way of Kings - Brandon Sanderson
- A Wizard of Earthsea - Ursula K. Le Guin

### Horror (3 books)
- The Shining - Stephen King
- House of Leaves - Mark Z. Danielewski
- Mexican Gothic - Silvia Moreno-Garcia

### Romance (3 books)
- Pride and Prejudice - Jane Austen
- The Notebook - Nicholas Sparks
- Red, White & Royal Blue - Casey McQuiston

### Thriller (3 books)
- Gone Girl - Gillian Flynn
- The Girl with the Dragon Tattoo - Stieg Larsson
- The Silent Patient - Alex Michaelides

### Sci-Fi (3 books)
- Dune - Frank Herbert
- Project Hail Mary - Andy Weir
- Neuromancer - William Gibson

### Documentary (3 books)
- Sapiens - Yuval Noah Harari
- Educated - Tara Westover
- The Immortal Life of Henrietta Lacks - Rebecca Skloot

## 🔧 Customization

### Adding More Books
Simply run the `populate_database.py` script again, or add books manually through Django admin.

### Styling
All CSS is embedded in the templates. You can:
- Modify colors in the `:root` CSS variables in `base.html`
- Adjust component styles in individual template files
- Add new utility classes in `base.html`

### Responsive Breakpoints
- Desktop: > 768px
- Mobile: ≤ 768px

## 📱 Responsive Design

All pages are fully responsive with:
- Flexible grid layouts using CSS Grid
- Mobile-first approach
- Touch-friendly buttons and links
- Optimized font sizes for mobile
- Collapsible navigation on small screens

## 🎓 Learning Objectives

This project helps you practice:
1. Django template inheritance and includes
2. Template variables and context
3. Loops and conditionals in templates
4. Modern CSS layout techniques (Grid, Flexbox)
5. Responsive design
6. CSS animations and transitions
7. Database population scripts
8. Django ORM queries

## 📄 License

This is an educational project for learning Django templates and modern web design.

---

**Made with ❤️ for Django learners**
