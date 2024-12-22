# Lab Manual: Performance Testing of a Local Web CRUD Application Using Locust

## Overview

This lab manual provides a comprehensive guide for conducting performance testing on a local web CRUD application using the Locust tool. It covers various types of performance testing, including load testing, stress testing, spike testing, and endurance testing.

## Background Theory

### What is Performance Testing?

Performance testing evaluates the speed, scalability, and stability of a software application under a specified workload. It is essential to ensure that applications can handle both expected and unexpected user loads without performance degradation.

### Types of Performance Testing

1. **Load Testing**: Assesses application behavior under normal load conditions.
2. **Stress Testing**: Identifies the application's breaking point with extreme loads.
3. **Spike Testing**: Tests the application’s response to sudden increases in load.
4. **Endurance Testing**: Evaluates stability and performance over an extended period.

## Introduction to Locust

Locust is an open-source load testing tool that allows users to define user behavior in Python code. Key features include:

- Easy to use with Python code.
- Scalability to simulate thousands of users.
- Web-based UI for real-time monitoring.

## Structured Approach to Performance Testing

### Load Testing

**User Story**: Assess system performance under normal load.

**Test Cases**:
- Create User
- Retrieve Users
- Update User
- Delete User

**Implementation**: See `load_test.py`.

### Stress Testing

**User Story**: Identify the system's breaking point.

**Test Cases**:
- High Concurrent Requests
- Rapid User Creation
- Frequent Updates
- Frequent Deletions

**Implementation**: See `stress_test.py`.

### Spike Testing

**User Story**: Test system response to sudden traffic spikes.

**Test Cases**:
- Create Users During Spike
- Retrieve Users During Spike

**Implementation**: See `spike_test.py`.

### Endurance Testing

**User Story**: Evaluate system performance over time.

**Test Cases**:
- Continuous Retrieval
- Continuous User Creation

**Implementation**: See `endurance_test.py`.

## Running Each Test

### Precondition

Start the application server using:
```bash
python app_using_json_server.py
or
python app_using_sqlite_server.py

### Execute Tests
Load Test: locust -f load_test.py --host=http://127.0.0.1:5000
Stress Test: locust -f stress_test.py --host=http://127.0.0.1:5000
Spike Test: locust -f spike_test.py --host=http://127.0.0.1:5000
Endurance Test: locust -f endurance_test.py --host=http://127.0.0.1:5000