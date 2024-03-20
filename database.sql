INSERT INTO Products (ProductID, ProductName, ProductDescription, Category)
VALUES (1, 'Milk', 'Fresh cow milk, 1 liter', 'Dairy'),
       (2, 'Toothpaste', 'Mint flavored toothpaste, 100ml', 'Personal Care'),
       (3, 'Chips', 'Cheese flavored chips, 200g', 'Snacks'),
       (4, 'Cooking Oil', 'Vegetable oil, 1 liter', 'Grocery'),
       (5, 'Coca Cola', 'Coca Cola, 1.5 liter', 'Beverages');

INSERT INTO Prices (ProductID, Price)
VALUES (1, 48),
       (2, 68),
       (3, 20),
       (4, 119),
       (5, 45);

INSERT INTO Discounts (ProductID, Discount, StartDate, EndDate)
VALUES (1, 0.05, '2022-01-01', '2022-12-31'),
       (3, 0.10, '2022-05-01', '2022-05-31'),
       (5, 0.07, '2022-06-01', '2022-06-30');

INSERT INTO Availability (ProductID, QuantityInStock)
VALUES (1, 100),
       (2, 200),
       (3, 300),
       (4, 150),
       (5, 250);
