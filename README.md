# 🚀 Python FastAPI REST API with CI/CD

A professional-grade REST API project demonstrating automated testing and continuous deployment.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Framework:** FastAPI
* **Testing:** Pytest & HTTPX
* **CI/CD:** GitHub Actions
* **Hosting:** Render

## 🔄 The Pipeline
This project uses a fully automated CI/CD workflow:
1. **Push:** Code is pushed to the `main` branch.
2. **CI (Continuous Integration):** GitHub Actions triggers a workflow that installs dependencies and runs automated tests via `pytest`.
3. **CD (Continuous Deployment):** If the tests pass, Render automatically pulls the latest code and deploys it to the live environment.



## 🌐 Live Demo
* **API Root:** [https://rest-api-l6q6.onrender.com/](https://rest-api-l6q6.onrender.com/)
* **Interactive Docs:** [https://rest-api-l6q6.onrender.com/docs](https://rest-api-l6q6.onrender.com/docs)

## 💻 Local Setup
1. Clone the repo:
   ```bash
   git clone [https://github.com/farazbaig01/REST_API.git](https://github.com/farazbaig01/REST_API.git)