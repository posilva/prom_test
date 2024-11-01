"""Prometheus metrics exporter package."""

__version__ = "0.1.0"

# prometheus_metrics/main.py
from prometheus_client import start_http_server, Gauge
import random
import time

# Create a gauge metric
temperature_gauge = Gauge(
    "room_temperature_celsius",
    "Current room temperature in Celsius",
    labelnames=["location"]
)

def generate_temperature():
    """Simulate temperature changes for different rooms."""
    locations = ["living_room", "bedroom", "kitchen"]
    
    while True:
        for location in locations:
            # Simulate temperature between 20-25°C with some random fluctuation
            temperature = 22.5 + random.uniform(-2.5, 2.5)
            
            # Set the gauge to the new temperature value with location label
            temperature_gauge.labels(location=location).set(temperature)
            
            print(f"Temperature in {location}: {temperature:.2f}°C")
        
        time.sleep(5)  # Wait for 5 seconds before next update

def main():
    """Main entry point for the application."""
    # Start up the server to expose the metrics
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    
    # Generate some metrics
    try:
        generate_temperature()
    except KeyboardInterrupt:
        print("\nMetrics collection stopped")

if __name__ == "__main__":
    main()
