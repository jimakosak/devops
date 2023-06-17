# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY server.py /app/

# Install the required dependencies
RUN pip install --no-cache-dir Flask boto3

# Expose the port on which the application will run
EXPOSE 4545

# Set environment variables
ENV AWS_ACCESS_KEY_ID="AKIAQ7SKPVPXPHGLOUG7"
ENV AWS_SECRET_ACCESS_KEY="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"

# Start the application
CMD ["python3", "server.py"]
