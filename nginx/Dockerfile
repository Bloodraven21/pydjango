# Use the official Nginx image
FROM nginx:latest

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom configuration file
COPY nginx.conf /etc/nginx/conf.d/

# Copy static files
#COPY ./volumes/static /app/static

# Copy media files
#COPY ./volumes/media /app/media

# Expose port 80
EXPOSE 80
