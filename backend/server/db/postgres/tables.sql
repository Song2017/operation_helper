 create table "app_authentication" (
    "app_authentication_id" serial primary key,

    "type" varchar(100),
    "platform" varchar,
    "token" varchar,
    "is_enabled" boolean default true,
    
    "create_time" timestamp(3) with time zone default current_timestamp,
    "modify_time" timestamp(3) with time zone default current_timestamp,
    "create_by" varchar(100),
    "modify_by" varchar(100)
);
comment on column app_authentication.type is 'APP authentication type: sms, code';

create table "app_operation_info" (
    "app_operation_info_id" serial primary key,

    "name" varchar(100),
    "description" varchar(100),
    "content" varchar,
    "is_consumed" boolean default false,

    "create_time" timestamp(3) with time zone default current_timestamp,
    "modify_time" timestamp(3) with time zone default current_timestamp,
    "create_by" varchar(100),
    "modify_by" varchar(100)
);

create table "app_user" (
    "app_user_id" serial primary key,

    "full_name" varchar(100),
    "email" varchar(100),
    "hashed_password" varchar,
    "is_active" boolean default true,
    "is_superuser" boolean default false,

    "create_time" timestamp(3) with time zone default current_timestamp,
    "modify_time" timestamp(3) with time zone default current_timestamp,
    "create_by" varchar(100),
    "modify_by" varchar(100)
);