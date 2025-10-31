# Tatana Blog - Photo Stories Platform

A modern, minimalist photo-sharing platform where users can share beautiful moments, stories, and connect through comments and likes.

## ✨ Features

### 🎨 Modern Design
- Clean, minimalist interface with custom CSS
- Photo-focused grid layout
- Responsive design for all devices
- Beautiful typography with Inter font

### 📸 Photo Sharing
- Upload and share multiple photos per post
- Location tagging for photo collections
- Rich text descriptions and stories
- Individual image captions
- Image optimization and display
- Delete individual images from posts

### 👤 User Profiles
- Custom user profiles with avatars
- Personal bio and location
- Website links
- User photo galleries

### ❤️ Social Features
- Like/unlike posts with real-time updates
- Comment system with user avatars
- User profile pages
- Social interactions

### 🗺️ Location Features
- Add location to posts
- Display location on posts and profiles
- Location-based browsing

## 🚀 Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   - Tatana Blog: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📱 Usage

### For Visitors
- Browse beautiful photo stories
- View user profiles
- See photo locations and details

### For Registered Users
- Share photos with stories and locations
- Like and comment on posts
- Create and customize your profile
- Edit your own posts
- Follow other users' stories

### For Administrators
- Manage all content through Django admin
- Moderate posts and comments
- Manage user accounts

## 🏗️ Project Structure

```
tatana-blog/
├── blog/                 # Main application
│   ├── models.py        # Post, Comment, UserProfile models
│   ├── views.py         # All view logic
│   ├── forms.py         # Forms for posts, comments, profiles
│   ├── templates/       # HTML templates
│   └── admin.py         # Admin configuration
├── blog_project/        # Django project settings
├── media/              # User uploaded files
│   ├── posts/          # Post images
│   └── avatars/        # Profile avatars
├── static/             # Static files
│   └── css/            # Custom CSS
└── requirements.txt    # Dependencies
```

## 🎯 Models

### UserProfile
- Avatar image upload
- Bio and personal information
- Location and website
- Linked to Django User model

### Post
- Title and content
- Multiple image uploads via PostImage model
- Location tagging
- Like system (many-to-many with users)
- Author and timestamps

### PostImage
- Individual images linked to posts
- Optional captions for each image
- Ordering system for image display
- Individual image management

### Comment
- Linked to posts and users
- Threaded commenting system
- Timestamps

## 🎨 Design Philosophy

Tatana Blog focuses on:
- **Minimalism:** Clean, distraction-free interface
- **Photo-first:** Images are the hero of every post
- **Social connection:** Easy ways to interact and connect
- **Beautiful typography:** Readable and elegant text
- **Mobile-friendly:** Works perfectly on all devices

## 🔧 Technologies Used

- **Backend:** Django 5.2, Python
- **Frontend:** Custom CSS, Feather Icons, Inter Font
- **Database:** SQLite (development)
- **Media:** Pillow for image processing
- **Authentication:** Django's built-in auth system