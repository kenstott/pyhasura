--
-- PostgreSQL database dump
--

-- Dumped from database version 15.6
-- Dumped by pg_dump version 15.7 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Customers; Type: TABLE; Schema: public; Owner: kenstott
--

CREATE TABLE public."Customers" (
    "customerKey" bigint,
    gender text,
    name text,
    city text,
    "stateCode" text,
    state text,
    "zipCode" text,
    country text,
    continent text,
    birthday timestamp without time zone
);


ALTER TABLE public."Customers" OWNER TO kenstott;

--
-- Name: DataDictionary; Type: TABLE; Schema: public; Owner: kenstott
--

CREATE TABLE public."DataDictionary" (
    "table" text,
    field text,
    description text
);


ALTER TABLE public."DataDictionary" OWNER TO kenstott;

--
-- Name: ExchangeRates; Type: TABLE; Schema: public; Owner: kenstott
--

CREATE TABLE public."ExchangeRates" (
    date timestamp without time zone,
    currency text,
    exchange double precision
);


ALTER TABLE public."ExchangeRates" OWNER TO kenstott;

--
-- Name: Products; Type: TABLE; Schema: public; Owner: kenstott
--

CREATE TABLE public."Products" (
    "productKey" bigint,
    "productName" text,
    brand text,
    color text,
    "unitCostUSD" double precision,
    "unitPriceUSD" double precision,
    "subcategoryKey" bigint,
    subcategory text,
    "categoryKey" bigint,
    category text
);


ALTER TABLE public."Products" OWNER TO kenstott;

--
-- Name: Sales; Type: TABLE; Schema: public; Owner: kenstott
--

CREATE TABLE public."Sales" (
    "orderNumber" bigint,
    "lineItem" bigint,
    "orderDate" timestamp without time zone,
    "deliveryDate" timestamp without time zone,
    "customerKey" bigint,
    "storeKey" bigint,
    "productKey" bigint,
    quantity bigint,
    "currencyCode" text
);


ALTER TABLE public."Sales" OWNER TO kenstott;

--
-- Name: Stores; Type: TABLE; Schema: public; Owner: kenstott
--

CREATE TABLE public."Stores" (
    "storeKey" bigint,
    country text,
    state text,
    "squareMeters" double precision,
    "openDate" timestamp without time zone
);


ALTER TABLE public."Stores" OWNER TO kenstott;

--
-- Name: z; Type: TABLE; Schema: public; Owner: kenstott
--

CREATE TABLE public.z (
    z boolean
);


ALTER TABLE public.z OWNER TO kenstott;

--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: cloud_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE cloud_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO neon_superuser WITH GRANT OPTION;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: cloud_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE cloud_admin IN SCHEMA public GRANT ALL ON TABLES  TO neon_superuser WITH GRANT OPTION;


--
-- PostgreSQL database dump complete
--

