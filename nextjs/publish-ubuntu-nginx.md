# publish a Next.js TypeScript project on an Ubuntu server with Nginx

This guide assumes you have basic knowledge of SSH, command line, and server management.

### Step 1: Prepare Your Next.js Project

1. **Build your Next.js project**:
   From your project directory, run:
   ```bash
   npm run build
   ```
   This will create a `build` folder with the production-ready files.

2. **Export the project (if needed)**:
   If your project uses static generation, you might want to export it:
   ```bash
   npm run export
   ```
   This will create an `out` folder with static files.

### Step 2: Set Up the Ubuntu Server

1. **Connect to your Ubuntu server**:
   Use SSH to connect to your server:
   ```bash
   ssh username@your_server_ip
   ```

2. **Update and upgrade your system**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

3. **Install Node.js and npm**:
   ```bash
   sudo apt install nodejs npm -y
   ```

4. **Install PM2 (optional but recommended for managing Node.js processes)**:
   ```bash
   sudo npm install pm2 -g
   ```

### Step 3: Deploy Your Next.js Application

1. **Transfer your project to the server**:
   Use `scp` or a tool like `rsync` to transfer your project files to the server. For example:
   ```bash
   scp -r /path/to/your/project username@your_server_ip:/path/to/server/directory
   ```

2. **Navigate to your project directory on the server**:
   ```bash
   cd /path/to/server/directory
   ```

3. **Install dependencies**:
   ```bash
   npm install
   ```

4. **Start your Next.js application**:
   If you're using PM2:
   ```bash
   pm2 start npm --name "your-app-name" -- start
   ```
   Otherwise, you can start it manually:
   ```bash
   npm start
   ```

### Step 4: Set Up Nginx as a Reverse Proxy

1. **Install Nginx**:
   ```bash
   sudo apt install nginx -y
   ```

2. **Create a new Nginx configuration file**:
   ```bash
   sudo nano /etc/nginx/sites-available/your-app-name
   ```

   Add the following configuration (adjust as necessary):
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;

       location / {
           proxy_pass http://localhost:3000;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

3. **Enable the new configuration**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/your-app-name /etc/nginx/sites-enabled/
   ```

4. **Test Nginx configuration and restart**:
   ```bash
   sudo nginx -t
   sudo systemctl restart nginx
   ```

### Step 5: Set Up a Process Manager (Optional but Recommended)

If you're using PM2, make sure it starts on system boot:
```bash
pm2 startup
pm2 save
```

### Step 6: Final Checks

1. **Check if your application is running**:
   Visit your domain in a web browser to ensure everything is working correctly.

2. **Monitor logs**:
   Use PM2 or check Nginx logs to troubleshoot any issues:
   ```bash
   pm2 logs your-app-name
   sudo tail -f /var/log/nginx/error.log
   ```

By following these steps, you should have your Next.js TypeScript project successfully deployed on an Ubuntu server with Nginx as a reverse proxy.