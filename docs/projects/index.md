---
hide:
- toc
- feedback

permalink: /projects/
---
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Primary Meta Tags -->
    <title>Harminder's Current Projects</title>
    <meta name="title" content="Harminder's Current Projects">
    <meta name="description" content="Explore Harminder Singh Nijjar's current projects">

    <!-- Google icons -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

    <!-- Tailwind CSS -->
    <link href="https://unpkg.com/tailwindcss@latest/dist/tailwind.min.css" rel="stylesheet">

    <!-- Favicon -->
    <link rel="shortcut icon" href="https://www.mkdocs.org/favicon.ico" type="image/x-icon">

    <!-- Custom styles -->
    <link rel="stylesheet" href="css/custom.css">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body>
    <div class="container mx-auto p-8">
        <div class="flex flex-wrap -m-4">
            <!-- Personal Site -->
            <div class="p-4 md:w-1/3">
                <div class="flex rounded-lg h-full bg-blue-300 p-8 flex-col transform transition duration-300 hover:shadow-xl hover:-translate-y-1">
                    <div class="flex items-center mb-3">
                        <h2 class="text-gray-900 text-lg title-font font-medium">Personal Site</h2>
                    </div>
                    <div class="flex-grow">
                        <p class="leading-relaxed text-base">Continuously updating my blog and portfolio site using MkDocs and Material for MkDocs.</p>
                        <a class="mt-3 text-blue-700 inline-flex items-center">Learn More
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                <path d="M5 12h14M12 5l7 7-7 7"></path>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Social Media Automation -->
            <div class="p-4 md:w-1/3">
                <div class="flex rounded-lg h-full bg-green-300 p-8 flex-col transform transition duration-300 hover:shadow-xl hover:-translate-y-1">
                    <div class="flex items-center mb-3">
                        <h2 class="text-gray-900 text-lg title-font font-medium">Social Media Automation</h2>
                    </div>
                    <div class="flex-grow">
                        <p class="leading-relaxed text-base">Working on automation solutions for social media platforms using Python and Playwright.</p>
                        <a class="mt-3 text-green-700 inline-flex items-center">Learn More
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                <path d="M5 12h14M12 5l7 7-7 7"></path>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>

            <!-- YouTube Clone -->
            <div class="p-4 md:w-1/3">
                <div class="flex rounded-lg h-full bg-red-300 p-8 flex-col transform transition duration-300 hover:shadow-xl hover:-translate-y-1">
                    <div class="flex items-center mb-3">
                        <h2 class="text-gray-900 text-lg title-font font-medium">ElevenLabs YouTube Chrome extension</h2>
                    </div>
                    <div class="flex-grow">
                        <p class="leading-relaxed text-base">Developing a Chrome extension to streamline the experience of watching dubbed content on YouTube.</p>
                        <a class="mt-3 text-red-700 inline-flex items-center">Learn More
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                <path d="M5 12h14M12 5l7 7-7 7"></path>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // JavaScript function to handle project card clicks
        function openProject(projectId) {
            console.log("Project Opened:", projectId);
            window.location.href = `/${projectId}`;
        }
    </script>

</body>

</html>
