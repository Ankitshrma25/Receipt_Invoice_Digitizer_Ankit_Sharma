# Receipt & Invoice Digitizer

A full-stack web application for digitizing, managing, and analyzing receipts and invoices with a modern React frontend and FastAPI backend.

## 🚀 Features

- **Digital Receipt Management**: Upload and store receipts and invoices digitally
- **Google OAuth Authentication**: Secure login with Google accounts
- **Data Extraction**: Automated extraction of receipt/invoice details
- **PDF Generation**: Export data as PDF reports with professional formatting
- **Dashboard Analytics**: Visual charts and insights for expense tracking
- **File Upload**: Support for multiple file formats
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS

## 📋 Tech Stack

### Frontend
- **React 18.2** - UI library
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client for API communication
- **Google OAuth** - Authentication
- **jsPDF & html2canvas** - PDF generation
- **Recharts** - Data visualization
- **Framer Motion** - Animations
- **Radix UI** - Accessible component primitives
- **TypeScript** - Type safety (in dev setup)

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **Python-Jose** - JWT token handling
- **Passlib with Bcrypt** - Password hashing
- **SQLite** - Lightweight database
- **Python-multipart** - File upload handling
- **Python-dotenv** - Environment variable management

## 📁 Project Structure

```
Receipt_Invoice_Digitizer_Ankit_Sharma/
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable React components
│   │   ├── pages/          # Page components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── services/       # API service calls
│   │   ├── lib/            # Utility functions
│   │   ├── utils/          # Helper utilities
│   │   ├── styles/         # CSS styles
│   │   ├── App.jsx         # Root app component
│   │   └── main.jsx        # Entry point
│   ├── package.json        # Frontend dependencies
│   └── vite.config.js      # Vite configuration
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI application entry
│   │   ├── models.py       # Database models
│   │   ├── api/            # API endpoints/routes
│   │   ├── core/           # Core utilities (auth, config)
│   │   ├── db/             # Database configuration
│   │   ├── repositories/   # Data access layer
│   │   ├── schemas/        # Pydantic schemas for validation
│   │   └── services/       # Business logic
│   ├── uploads/            # Uploaded file storage
│   ├── requirements.txt    # Python dependencies
│   ├── .env                # Environment variables
│   └── app.db              # SQLite database
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🛠️ Getting Started

### Prerequisites
- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn** (for frontend)
- **pip** (for backend)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the backend directory with necessary environment variables:
```
DATABASE_URL=sqlite:///app.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

6. Run the backend server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the frontend directory (if needed):
```
VITE_API_URL=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
```

4. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### Building for Production

**Frontend:**
```bash
npm run build
npm run preview
```

**Backend:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📚 API Endpoints

The backend provides RESTful API endpoints. Full documentation is available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

Common endpoints include:
- **Authentication**: Login, register, token refresh
- **Receipts/Invoices**: CRUD operations
- **File Upload**: Upload receipt/invoice files
- **Analytics**: Get expense data and charts
- **Profile**: User information management

## 🔐 Authentication

The application uses:
- **Google OAuth** for frontend authentication
- **JWT tokens** for API authentication
- **Bcrypt password hashing** for secure storage

## 📦 Environment Variables

### Backend (.env)
```
DATABASE_URL=sqlite:///app.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-oauth-client-id
```

## 🚀 Development Workflow

1. **Frontend Development**: Run `npm run dev` for hot module reloading
2. **Backend Development**: Use `uvicorn` with `--reload` flag for auto-reload
3. **Database**: SQLite database is automatically created on first run
4. **API Testing**: Use Swagger UI at `/docs` endpoint

## 📝 Scripts

### Frontend Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Backend Scripts
- `uvicorn app.main:app --reload` - Start development server
- `python -m pytest` - Run tests (if configured)

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Create a pull request

## 📄 License

Check the LICENSE file for license information.

## 👤 Author

**Ankit Sharma**

## 📧 Support

For issues or questions, please open an issue in the repository.

---

**Happy Digitizing!** 📄✨
