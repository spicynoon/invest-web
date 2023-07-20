# Base image
FROM debian:bullseye-slim

# Install dependencies
RUN apt-get update && apt-get install -y git neovim netcat python3-pip

# Copy web service files
COPY invest-app.py /home/investyu/invest-app
COPY requirements.txt /home/investyu/requirements.txt

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /home/investyu/requirements.txt

# Set working directory
WORKDIR /home/investyu

# Expose port
EXPOSE 25144

# Start web service
CMD ["streamlit", "run", "--server.port=25144", "invest-app.py"]