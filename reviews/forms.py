from django import forms
from reviews.models import Review
from books.models import Book


class ReviewFormBase(forms.ModelForm):
    delivery_method = forms.ChoiceField(
        choices=[
            ('email', 'Email Notification'),
            ('sms', 'SMS Notification'),
            ('none', 'No Notification'),
        ],
        required=False,
        label='Notification Method'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all()
        self.fields['book'].required = False

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['created_at']

        help_texts = {
            'body': 'Write your review here.',
            'rating': 'Rate the book from 0 to 10.',
            'author': 'Enter your name.',
        }
        labels = {
            'author': 'Reviewer Name',
            'body': 'Review Content',
            'rating': 'Rating (0-10)',
            'book': 'Book',
        }
        widgets = {
            'body': forms.Textarea,
            'rating': forms.NumberInput,
            'author': forms.TextInput,
            'book': forms.Select,
        }
        initial = {
            'rating': 5.00,
        }


class ReviewFormCreate(ReviewFormBase):
    pass


class ReviewFormEdit(ReviewFormBase):
    pass


class ReviewFormDelete(ReviewFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
