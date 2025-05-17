CREATE TABLE BB_Clients (
    ClientID INT PRIMARY KEY IDENTITY(1,1),   -- PK
    ClientName VARCHAR(100) NOT NULL,               -- Name
    Email VARCHAR(100),                       -- E-mail
    Birthday DATE,                            -- Birthday
    Gender CHAR(1),                           -- Gender as: M (male), F (female), O (others)
    CPF VARCHAR(14),                          -- CPF fictício (brazilian SSN), format '000.000.000-00'
    Telephone VARCHAR(20),                    -- Telephone 
    HouseAddress VARCHAR(255),                -- Client Address
    City VARCHAR(100),                        -- Client City
    ClientState CHAR(2),                           -- Client State ID, ex: 'SP', 'RJ', 'NY'
    RegisterDate DATE DEFAULT GETDATE(),      -- Register date on system
    StatusClient VARCHAR(20) DEFAULT 'Ativo'  -- Active, Inactive, Blocked, etc...
);
