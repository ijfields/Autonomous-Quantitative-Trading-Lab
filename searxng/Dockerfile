# Use the official image as base
FROM searxng/searxng:latest

# Switch to root to perform operations
USER root

# Copy the settings file from your host into the image
COPY settings.yml /etc/searxng/settings.yml

# Force correct permissions permanently
RUN chown searxng:searxng /etc/searxng/settings.yml && \
    chmod 644 /etc/searxng/settings.yml

# Switch back to the searxng user
USER searxng
