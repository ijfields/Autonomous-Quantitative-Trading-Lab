
import { Pool } from 'pg';

const poolConfig = {
    user: process.env.POSTGRES_USER || 'myuser',
    password: process.env.POSTGRES_PASSWORD || 'mypassword',
    host: process.env.DB_HOST || 'localhost',
    port: parseInt(process.env.DB_PORT || '5432'),
    database: process.env.POSTGRES_DB || 'trading_db',
};

let pool: Pool;

if (process.env.NODE_ENV === 'production') {
    pool = new Pool(poolConfig);
} else {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    if (!(global as any).postgresPool) {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        (global as any).postgresPool = new Pool(poolConfig);
    }
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    pool = (global as any).postgresPool;
}

export default pool;
