/** @type {import('next').NextConfig} */
const nextConfig = {
    webpack: (config) => {
        config.externals.push(
            "pino-pretty",
            "lokijs",
            "encoding",
            "osx-temperature-sensor",
            "macos-temperature-sensor"
        );
        return config;
    },
    eslint: {
        ignoreDuringBuilds: true,
    },
};

export default nextConfig;
