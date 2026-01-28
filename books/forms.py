from django import forms

from books.choices import GenreTextChoices
from books.models import Tag, Book


# class BookFormBasic(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['tag'].choices = [ (tag.id, tag.name) for tag in Tag.objects.all() ]
#
#     title = forms.CharField(
#         max_length=100,
#         required=True,
#         label="Title",
#         help_text="Max length 100 characters.",
#     )
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         required=True,
#         label="Price ($)",
#         initial=0.00,
#     )
#     isbn = forms.CharField(
#         max_length=12,
#         required=True,
#         label="ISBN",
#         error_messages={
#             'unique': "A book with this ISBN already exists.",
#             'max_length': "ISBN cannot exceed 12 characters.",
#         }
#     )
#     genre = forms.ChoiceField(
#         choices = GenreTextChoices,
#         label="Genre",
#         widget=forms.Select
#     )
#     publishing_date = forms.DateField(
#         required=False,
#         label="Published Date",
#         widget=forms.DateInput
#     )
#     description = forms.CharField(
#         required=False,
#         label="Description",
#         widget=forms.Textarea
#     )
#     image_url = forms.URLField(
#         required=False,
#         label="Image URL",
#         widget=forms.URLInput
#     )
#     author = forms.CharField(
#         max_length=100,
#         required=True,
#         label="Author"
#     )
#     country = forms.CharField(
#         max_length=50,
#         required=False,
#         label="Country"
#     )
#
#     tag = forms.ChoiceField(
#         required=False,
#         label="Tags"
#     )


class BookFormBase(forms.ModelForm):
    payment_method = forms.ChoiceField(
        choices=[
            ('credit_card', 'Credit Card'),
            ('paypal', 'PayPal'),
            ('bank_transfer', 'Bank Transfer'),
        ],
        required=False,
        label='Payment Method',

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tag'].queryset = Tag.objects.all()
        self.fields['image_url'].required = False


    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['slug', 'updated_at']

        help_texts = {
            'image_url': 'Enter a valid URL for the book cover image.',
            'publishing_date': 'Select the date when the book was published.',
            'description': 'Provide a brief description of the book.',
        }
        labels = {
            'image_url': 'Image URL',
            'publishing_date': 'Published Date',
            'description': 'Description',
            'title': 'Title',
            'price': 'Price ($)',
            'isbn': 'ISBN',
            'author': 'Author',
            'country': 'Country',
            'genre': 'Genre',
            'tag': 'Tags',
            'available': 'Available',
            'pages': 'Number of Pages',
        }
        widgets = {
            'tag': forms.CheckboxSelectMultiple,
            'publishing_date': forms.DateInput,
            'description': forms.Textarea,
            'image_url': forms.URLInput,
            'genre': forms.Select,
            'available': forms.CheckboxInput,
            'pages': forms.NumberInput
        }
        initial = {
            'price': 0.00,
            'available': True,
        }

class BookFormCreate(BookFormBase):
    pass

class BookFormEdit(BookFormBase):
    pass

class BookFormDelete(BookFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

class BookSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'},)
    )
