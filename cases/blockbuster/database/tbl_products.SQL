CREATE TABLE BB_Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),               -- Unique product ID
    Title VARCHAR(255) NOT NULL,                           -- Movie/series title
    Type VARCHAR(10) CHECK (Type IN ('Movie', 'Series')),  -- Type of content
    Genre VARCHAR(50),                                     -- Genre: Action, Comedy, etc.
    DurationMinutes INT,                                   -- Duration in minutes
    Rating VARCHAR(10),                                    -- Age rating: 'G', 'PG-13', 'R', etc.
    ReleaseYear INT,                                       -- Year of release
    Stock INT DEFAULT 0,                                   -- Number of available units
    SalePrice DECIMAL(10, 2),                              -- Price for sale
    RentalPrice DECIMAL(10, 2),                            -- Price for rental
    IsActive BIT DEFAULT 1                                 -- 1 = active, 0 = inactive
);