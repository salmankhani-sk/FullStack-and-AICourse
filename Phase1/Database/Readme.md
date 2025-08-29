
##  Step 1: Install PostgreSQL

###  Download PostgreSQL
- Go to [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
- Select your operating system:
  - **Windows** → Use the EnterpriseDB installer (includes pgAdmin).
  

Install the **latest stable version** (recommended: PostgreSQL 16+).

---

##  Step 2: Install pgAdmin (GUI Tool)

- **pgAdmin** is a graphical tool for managing PostgreSQL.
- Comes bundled with PostgreSQL installer on Windows.
- If not installed, download from: [https://www.pgadmin.org/download/](https://www.pgadmin.org/download/)

We’ll use pgAdmin at the start since it’s beginner-friendly.

---

##  Step 3: Install Command-Line Tool ( Recommended)

- PostgreSQL comes with a tool called **psql** (Postgres Shell).
- This allows you to write SQL commands directly from the terminal.
- Don’t worry—we’ll start with GUI first and then move to CLI.

---

##  Step 4: (Optional) Install a Universal Database Client

You may also install tools like:
- **DBeaver** → [https://dbeaver.io/download/](https://dbeaver.io/download/)  
- **TablePlus** → [https://tableplus.com/](https://tableplus.com/)  

These tools work with PostgreSQL and many other databases.

---

## Verify Installation

After installation, check if PostgreSQL is installed correctly:

### 
```bash
psql --version

``
psql (PostgreSQL) 16.2

