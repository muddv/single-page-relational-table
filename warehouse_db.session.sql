-- @block
CREATE TABLE shipments(
    id INT PRIMARY KEY AUTO_INCREMENT,
    shipment_date DATE,
    item VARCHAR(255),
    amount INT,
    shipment_distance INT
);

-- @block
INSERT INTO shipments(shipment_date, item, amount, shipment_distance)
VALUES 
    ('2025-11-11', 'cheese', '99999', '888'),
    ('2025-10-11', 'apples', '56456', '100'),
    ('2025-09-01', 'melons', '246324', '51'),
    ('2026-01-05', 'avocados', '448', '234'),
    ('2025-09-11', 'corn', '324534', '643'),
    ('2025-08-11', 'bananas', '2435', '633');
