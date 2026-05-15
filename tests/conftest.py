"""
Pytest configuration and shared fixtures for officeGraph tests
"""
import pytest


@pytest.fixture
def sample_employee_data():
    """Sample employee data for testing"""
    return {
        'first_name': 'Michael',
        'last_name': 'Scott',
        'position': 'Regional Manager',
        'department': 'Management'
    }


@pytest.fixture
def invalid_employee_data():
    """Invalid employee data for testing validation"""
    return {
        'first_name': 'Michael123',  # Invalid characters
        'last_name': 'Scott!@#',     # Invalid characters
        'position': '',               # Empty position
        'department': 'Sales'
    }
