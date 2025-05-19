# Coffee Shop Domain Modeling

### **Assessment**  
**Code Challenge - Coffee Shop (Object Relationships)**  

---

## **Objective**  
Create a Python application using object-oriented programming (OOP) principles to model a Coffee Shop domain. This project tests your ability to design classes, implement methods, establish relationships between objects, and handle data appropriately.  

---

## **Project Overview**  
The Coffee Shop domain consists of three main entities:  

- **Customer:** Represents a coffee shop customer.  
- **Coffee:** Represents a type of coffee available at the shop.  
- **Order:** Represents a specific customer order, linking a customer and a coffee.  

### **Relationships**  
- A **Customer** can place many **Orders**.  
- A **Coffee** can have many **Orders**.  
- An **Order** belongs to one **Customer** and one **Coffee**.  
- **Customer** and **Coffee** have a many-to-many relationship through **Order**.  

---

## **Setup and Installation**  
1. **Create Project Directory:**  
   ```bash
   mkdir coffee_shop
   cd coffee_shop
   ```  

2. **Set Up Virtual Environment:**  
   ```bash
   pipenv install  
   pipenv shell  
   ```  

3. **Install Testing Tools:**  
   ```bash
   pipenv install pytest  
   ```  

---

## **Class Design**  
### **Customer (`customer.py`)**  
- **Attributes:**  
  - `name` (String, 1 to 15 characters)  
- **Methods:**  
  - `orders()` - Returns all orders placed by the customer.  
  - `coffees()` - Returns a unique list of coffees the customer has ordered.  
  - `create_order(coffee, price)` - Creates a new order for the customer.  

### **Coffee (`coffee.py`)**  
- **Attributes:**  
  - `name` (String, at least 3 characters long)  
- **Methods:**  
  - `orders()` - Returns all orders for the coffee.  
  - `customers()` - Returns a unique list of customers who ordered the coffee.  
  - `num_orders()` - Returns the total number of orders for the coffee.  
  - `average_price()` - Returns the average price of the coffee based on its orders.  

### **Order (`order.py`)**  
- **Attributes:**  
  - `customer` (Customer instance)  
  - `coffee` (Coffee instance)  
  - `price` (Float, 1.0 to 10.0)  
- **Methods:**  
  - `customer()` - Returns the customer who placed the order.  
  - `coffee()` - Returns the coffee associated with the order.  

---



## **Testing**  
1. **Run Tests:**  
   ```bash
   pytest  
   ```  

---

## **Debugging and Refactoring**  
- Use `debug.py` to interactively test your classes and methods.  
- Follow PEP 8 guidelines for clean, readable code.  

---

## **Submission**  
- Push your project to a private GitHub repository.  
- Add your TM as a collaborator.  
- Submit the repository link for grading.  

---

## **License**  
This project is licensed under the MIT License - see the LICENSE file for details.
