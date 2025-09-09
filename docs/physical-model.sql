CREATE TABLE "User" 
( 
 id SERIAL PRIMARY KEY,  
 name VARCHAR(100) NOT NULL,  
 phone_number VARCHAR(20) NOT NULL,  
 email VARCHAR(254) NOT NULL UNIQUE,  
 password VARCHAR(255) NOT NULL,  
 created_at DATE NOT NULL
); 

CREATE TABLE Exhibitor 
( 
 id SERIAL PRIMARY KEY,  
 contact_phone_number VARCHAR(20) NOT NULL,  
 contact_email VARCHAR(254) NOT NULL,  
 user_id INT NOT NULL, 
 CONSTRAINT fk_exhibitor_user FOREIGN KEY (user_id) REFERENCES "User" (id)
 
); 

CREATE TABLE Client 
( 
 id SERIAL PRIMARY KEY,  
 attended_tradefairs INT DEFAULT 0,  
 user_id INT NOT NULL,
 CONSTRAINT fk_client_user FOREIGN KEY (user_id) REFERENCES "User" (id)

); 

CREATE TABLE Admin 
( 
 id SERIAL PRIMARY KEY,  
 contact_email VARCHAR(254) NOT NULL,  
 managed_tradefairs_count INT DEFAULT 0,  
 user_id INT NOT NULL,  
 CONSTRAINT fk_admin_user FOREIGN KEY (user_id) REFERENCES "User" (id)
); 

CREATE TABLE TradeFair 
( 
 id SERIAL PRIMARY KEY,  
 name VARCHAR(100) NOT NULL,  
 description TEXT,  
 start_date DATE NOT NULL,  
 end_date DATE NOT NULL,  
 venue_name VARCHAR(100) NOT NULL,  
 street_address VARCHAR(100) NOT NULL,  
 city VARCHAR(100) NOT NULL,  
 created_at DATE NOT NULL,  
); 

CREATE TABLE Product 
( 
 id SERIAL PRIMARY KEY,  
 name VARCHAR(100) NOT NULL,  
 category VARCHAR(100),  
 quantity INT NOT NULL,  
 price NUMERIC(10,2) NOT NULL,  
 description TEXT NOT NULL,  
 exhibitor_id INT NOT NULL,  
 created_at DATE NOT NULL,  
 CONSTRAINT fk_product_exhibitor FOREIGN KEY (exhibitor_id) REFERENCES Exhibitor (id)

); 

CREATE TABLE Role 
( 
 id SERIAL PRIMARY KEY,  
 role_name VARCHAR(100) NOT NULL,  
); 

CREATE TABLE Booth 
( 
 id SERIAL PRIMARY KEY,  
 booth_number INT NOT NULL,  
 exhibitor_id INT,  
 tradefair_id INT,
 CONSTRAINT fk_booth_exhibitor FOREIGN KEY (exhibitor_id) REFERENCES Exhibitor (id),
 CONSTRAINT fk_booth_tradefair FOREIGN KEY (tradefair_id) REFERENCES TradeFair (id)  
); 

CREATE TABLE Attendence 
( 
 id SERIAL PRIMARY KEY,  
 status VARCHAR(100) NOT NULL,  
 registration_date DATE NOT NULL,  
 client_id INT NOT NULL,  
 tradefair_id INT NOT NULL,
 CONSTRAINT fk_attendance_client FOREIGN KEY (client_id) REFERENCES Client (id),
 CONSTRAINT fk_attendance_tradefair FOREIGN KEY (tradefair_id) REFERENCES TradeFair (id)  
); 

CREATE TABLE admins_tradefairs 
( 
 id SERIAL PRIMARY KEY,  
 admin_id INT NOT NULL,  
 tradefair_id INT NOT NULL,
 CONSTRAINT fk_admins_tradefairs_admin FOREIGN KEY (admin_id) REFERENCES Admin (id),
 CONSTRAINT fk_admins_tradefairs_tradefair FOREIGN KEY (tradefair_id) REFERENCES TradeFair (id)  
); 

CREATE TABLE roles_users 
( 
 id SERIAL PRIMARY KEY,  
 user_id INT NOT NULL,  
 role_id INT NOT NULL,
 CONSTRAINT fk_roles_users_user FOREIGN KEY (user_id) REFERENCES "User" (id),
 CONSTRAINT fk_roles_users_role FOREIGN KEY (role_id) REFERENCES Role (id)  
); 
