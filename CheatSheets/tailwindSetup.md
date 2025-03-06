## Navigate

[HOME](before_you_start.md)      

[Want to install TailWind?](tailwindSetup.md)

[Want to host you apps on Ubuntu?](hosting_on_Ubuntu.md)

[Video Titles](video_titles.md)

# *How to setup Tailwind CSS*

### *Step 1: Run the following commands*

```
npm install -D tailwindcss
npx tailwindcss init
```

*For PostCSS config file: postcss.config.js*

```
npx tailwindcss init -p
```

### *Step 2: Update tailwind.conf.js file to include this line:*

```
content: ["*.html"],
```

### *Step 3: create src/input.css to include:*

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### *Step 4: Include the src/output.css file to your html*

### *Step 5: Run the following command (This command should be run always you going to work):*

```
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```
.
_____
.
_____
.
_____
.
_____
.
_____
# *Setup Tailwind CSS for viteXreact app*

### *Step 1: Run the following commands*

```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### *Step 2: Replace tailwind.conf.js file with following content:*

```
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### *Step 3: Add the @tailwind directives for each of Tailwind’s layers to your ./src/index.css file.*

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### *Step 3: Start your build process*

```
npm run dev
```

