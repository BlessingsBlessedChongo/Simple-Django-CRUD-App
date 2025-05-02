# Task Manager - Simple Django CRUD Application


A simple yet powerful Task Manager web application built with Django that allows users to Create, Read, Update, and Delete (CRUD) tasks with a clean, responsive interface.

## Features

✅ **Full CRUD Functionality** - Create, view, edit, and delete tasks  
✅ **Task Prioritization** - Set priority levels (Low/Medium/High)  
✅ **Status Tracking** - Track task status (Not Started/In Progress/Completed)  
✅ **Due Dates** - Set and view task deadlines  
✅ **Responsive Design** - Works on all device sizes  
✅ **Visual Indicators** - Color-coded priorities and statuses  
✅ **User-Friendly Forms** - Intuitive form validation and layout  

## Technologies Used

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5, CSS3
- **Database**: SQLite (default)
- **Icons**: Bootstrap Icons

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/taskmanager.git
   cd taskmanager
   ```

2. **Create and activate virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```
   python manage.py runserver
   ```

7. **Access the application**
   - Frontend: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

## Project Structure

```
taskmanager/
├── tasks/                # Main app directory
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── admin.py          # Admin configuration
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   ├── urls.py           # App URLs
│   └── views.py          # View functions
├── taskmanager/          # Project settings
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URLs
│   └── wsgi.py           # WSGI config
├── .gitignore           # Git ignore file
├── manage.py            # Django management script
└── README.md            # This file
```

## Here is the Demo Video


https://github.com/user-attachments/assets/a3a96f2e-9b13-4d8b-8976-fc524b11bc26


<!-- Add your screenshots here if you have them -->


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact:  
Blessings B Chongo - blessingsblessedchongo@gmail.com
Project Link: https://github.com/blessingsblessedchongo/Simple-Django-CRUD-App
