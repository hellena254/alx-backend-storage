# Backend Storage Project

## Overview

This project explores advanced backend storage techniques using various database technologies. It covers MySQL for relational database management, NoSQL databases like MongoDB for document storage, and Redis for caching.

## Contents

### MySQL

- **Table Constraints**: Learn to create tables with constraints such as `NOT NULL`, `UNIQUE`, and `FOREIGN KEY`.
- **Query Optimization**: Improve query performance by adding indexes.
- **Stored Procedures & Functions**: Implement reusable code blocks for complex operations.
- **Views**: Create virtual tables to simplify complex queries.
- **Triggers**: Automate actions in response to database events.

### NoSQL

- **Concepts**: Understand NoSQL fundamentals and how it differs from SQL.
- **ACID**: Learn about Atomicity, Consistency, Isolation, and Durability.
- **Document Storage**: Explore document-based storage and its advantages.
- **Database Types**: Overview of various NoSQL database types.
- **Benefits**: Discover the benefits of using NoSQL databases.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations in NoSQL databases.
- **MongoDB**: Basic usage and operations for MongoDB.

### Redis

- **Basic Operations**: Learn fundamental Redis commands.
- **Caching**: Implement Redis as a simple cache.
- **Advanced Usage**: Track access counts and cache HTML content with expiration times.

## Installation

1. **Redis**: Install from [Redis.io](https://redis.io/download).
2. **MongoDB**: Install from [MongoDB's official site](https://www.mongodb.com/try/download/community).
3. **Python Dependencies**: Install using:
   ```bash
   pip install redis requests pymongo
   ```

## Usage

1. **Redis Operations**: Use provided scripts for basic Redis interactions and caching.
2. **MongoDB Operations**: Refer to example scripts for MongoDB queries and updates.
3. **MySQL Examples**: Explore MySQL scripts for advanced database management.
4. **Web Page Caching**: Run `web.py` to fetch and cache HTML content with Redis.

