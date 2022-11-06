# operation_helper
1. 验证码
接收验证码并保存
2. 自动化任务


# guide
## Development
Bring up app-database cluster:
```bash
docker-compose -f docker-compose.app.yml up
```

## PGAdmin
### Access to PgAdmin: 
* **URL:** [http://localhost:5050](http://localhost:5050)
* **Username:** user@domain.com (as a default)
* **Password:** SuperSecret (as a default)

### Add a new server in PgAdmin:
* **PostgresHost** as `POSTGRES_HOST`, by default: `kong-database`