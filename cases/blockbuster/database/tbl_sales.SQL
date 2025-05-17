CREATE TABLE BB_Sales (
    OperationID INT PRIMARY KEY IDENTITY(1,1),                       -- Unique operation ID
    ClientID INT FOREIGN KEY REFERENCES BB_Clients(ClientID),        -- FK to client
    ProductID INT FOREIGN KEY REFERENCES BB_Products(ProductID),     -- FK to product
    OperationType VARCHAR(10) CHECK (OperationType IN ('Sale', 'Rental')), -- Type of operation
    OperationDate DATE NOT NULL DEFAULT GETDATE(),                  -- Date of transaction
    AmountPaid DECIMAL(10, 2) NOT NULL,                             -- Total paid by client
    Returned BIT DEFAULT NULL                                       -- NULL or 0/1 for rental returns
);