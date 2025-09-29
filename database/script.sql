-- ================================
-- 🧱 CRIAÇÃO DAS TABELAS
-- ================================

-- brand definition
CREATE TABLE brand (
	id_brand INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

-- country definition
CREATE TABLE country (
	id_country INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	country_code INTEGER NOT NULL
);

-- status definition
CREATE TABLE status (
	id_status INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

-- state definition
CREATE TABLE state (
	id_state INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	fu TEXT NOT NULL,
	id_country INTEGER NOT NULL,
	CONSTRAINT state_country_FK FOREIGN KEY (id_country) REFERENCES country(id_country)
);

-- "type" definition
CREATE TABLE "type" (
	id_type INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_brand INTEGER NOT NULL,
	line TEXT NOT NULL,
	output_current TEXT NOT NULL,
	charging_voltage TEXT NOT NULL,
	maximum_power TEXT NOT NULL,
	number_of_outlets TEXT NOT NULL,
	model TEXT NOT NULL,
	CONSTRAINT type_brand_FK FOREIGN KEY (id_brand) REFERENCES brand(id_brand)
);

-- city definition
CREATE TABLE city (
	id_city INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	id_state INTEGER NOT NULL,
	CONSTRAINT city_state_FK FOREIGN KEY (id_state) REFERENCES state(id_state)
);

-- neighborhood definition
CREATE TABLE neighborhood (
	id_neighborhood INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	id_city INTEGER NOT NULL,
	CONSTRAINT neighborhood_city_FK FOREIGN KEY (id_city) REFERENCES city(id_city)
);

-- address definition
CREATE TABLE address (
	id_address INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	street TEXT NOT NULL,
	id_neighborhood INTEGER NOT NULL,
	postal_code TEXT NOT NULL,
	coordinates TEXT NOT NULL,
	CONSTRAINT address_neighborhood_FK FOREIGN KEY (id_neighborhood) REFERENCES neighborhood(id_neighborhood)
);

-- charger definition
CREATE TABLE charger (
	id_charger INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_type INTEGER NOT NULL,
	id_address INTEGER NOT NULL,
	id_status INTEGER NOT NULL,
	"timestamp" TEXT NOT NULL,
	CONSTRAINT charger_address_FK FOREIGN KEY (id_address) REFERENCES address(id_address),
	CONSTRAINT charger_status_FK FOREIGN KEY (id_status) REFERENCES status(id_status),
	CONSTRAINT charger_type_FK FOREIGN KEY (id_type) REFERENCES "type"(id_type)
);


-- ================================
-- ✅ INSERÇÃO DE DADOS (São José dos Campos - SP)
-- ================================

-- Inserir marcas (brand)
INSERT INTO brand (name) VALUES ('Tesla');
INSERT INTO brand (name) VALUES ('ABB');

-- Inserir países
INSERT INTO country (name, country_code) VALUES ('Brasil', 55);

-- Inserir status
INSERT INTO status (name) VALUES ('Ativo');
INSERT INTO status (name) VALUES ('Inativo');
INSERT INTO status (name) VALUES ('Manutenção');

-- Inserir estado (São Paulo)
INSERT INTO state (name, fu, id_country) VALUES ('São Paulo', 'SP', 1);

-- Inserir cidade (São José dos Campos)
INSERT INTO city (name, id_state) VALUES ('São José dos Campos', 1);

-- Inserir bairros
INSERT INTO neighborhood (name, id_city) VALUES ('Centro', 1);
INSERT INTO neighborhood (name, id_city) VALUES ('Jardim Aquarius', 1);
INSERT INTO neighborhood (name, id_city) VALUES ('Urbanova', 1);

-- Inserir endereços
INSERT INTO address (street, id_neighborhood, postal_code, coordinates) 
VALUES ('Rua XV de Novembro, 123', 1, '12210-150', '-23.1896,-45.8841');
INSERT INTO address (street, id_neighborhood, postal_code, coordinates) 
VALUES ('Av. Cassiano Ricardo, 500', 2, '12246-870', '-23.2236,-45.9005');
INSERT INTO address (street, id_neighborhood, postal_code, coordinates) 
VALUES ('Av. Shishima Hifumi, 291', 3, '12233-000', '-23.2284,-45.8876');

-- Inserir tipos de carregadores
INSERT INTO "type" (id_brand, line, output_current, charging_voltage, maximum_power, number_of_outlets, model)
VALUES (1, 'Wall Connector', '32A', '240V', '7.4kW', '1', 'WC-Gen3');
INSERT INTO "type" (id_brand, line, output_current, charging_voltage, maximum_power, number_of_outlets, model)
VALUES (2, 'Terra AC', '16A', '400V', '22kW', '2', 'Terra AC Wallbox');

-- Inserir carregadores
INSERT INTO charger (id_type, id_address, id_status, "timestamp") 
VALUES (1, 1, 1, '2025-09-23 10:00:00');
INSERT INTO charger (id_type, id_address, id_status, "timestamp") 
VALUES (2, 2, 3, '2025-09-23 11:30:00');
INSERT INTO charger (id_type, id_address, id_status, "timestamp") 
VALUES (1, 3, 2, '2025-09-22 08:45:00');
