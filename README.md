# Docker Compose

## Overview
This project uses Docker Compose to set up and run two containers:  
1. A **database container** (PostgreSQL).  
2. A **web application container** (Flask).

## Prerequisites
Before running this project, ensure you have the following installed on your system:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Usage

1. **Clone the Repository**  
   ```sh
   git clone https://github.com/mahmoudamr12/Konecta_Task03.git
   cd Konecta_Task03
   ```

2. **Start the Containers**  
   ```sh
   docker-compose up -d
   ```

3. **Verify Containers are Running**  
   ```sh
   docker ps
   ```

4. **Access the Web Application**  
   Open your browser and go to:  
   ```
   http://localhost // or the public IP address of the virtual machine you're using
   ```

## Screenshots

1. **Database and Web Containers Connection**  

   ![Image](https://github.com/user-attachments/assets/29c2e19d-d025-4399-937f-db30436d6057)

2. **Running Website**  

   ![Image](https://github.com/user-attachments/assets/68d20335-f515-4916-b25b-4b55df520733)
