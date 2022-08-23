drop table if exists public.forum22_ecommmerce;
create table public.forum22_ecommmerce AS
select * from json_to_recordset(
$$
[
	{"id": 15364, "language": null, "allow_feed": true, "name": "Marcela ", "email": null, "user_classification_name": null, "user_classification_id": 0, "cpf": "", "company": "Santander", "role": "Diretoria (C-Level)", "my_description": "", "matched": false, "match_id": null, "cellphone": null, "city": "S\u00e3o Paulo", "state": "S\u00e3o Paulo", "site": null, "points": 1350.0, "avatar": "/uploads/user/avatar/15364/normal_52b0a2e6-581a-4caa-86d5-0189cfc0e249.jpg", "avatar_thumb": "/uploads/user/avatar/15364/thumb_52b0a2e6-581a-4caa-86d5-0189cfc0e249.jpg", "requested": false, "attribute_1": "eae5de9f-a51e-4113-9bd2-cc30997733a6", "attribute_2": "", "attribute_3": "", "country": "Brasil", "birth": null, "sex": "", "hash_token": "e0fa671941dfc684753a26cf7b2d1d82"},
	{"id": 10075, "language": null, "allow_feed": true, "name": "Marco  ", "email": null, "user_classification_name": null, "user_classification_id": 0, "cpf": "", "company": "TOTVS S.A", "role": "Diretoria (C-Level)", "my_description": "", "matched": false, "match_id": null, "cellphone": null, "city": "Rio de Janeiro", "state": "Rio de Janeiro", "site": null, "points": 9400.0, "avatar": "/uploads/user/avatar/10075/normal_9f2e18f3-b0ab-4a27-b0d5-1f2325a6d7eb.jpg", "avatar_thumb": "/uploads/user/avatar/10075/thumb_9f2e18f3-b0ab-4a27-b0d5-1f2325a6d7eb.jpg", "requested": false, "attribute_1": "b507c79c-732e-4001-b210-e1fa4d02a787", "attribute_2": "", "attribute_3": "", "country": "Brasil", "birth": null, "sex": "", "hash_token": "e7bdd363ca667077d92bafaf5a94c945"},
	{"id": 8482, "language": null, "allow_feed": true, "name": "Chaline ", "email": null, "user_classification_name": null, "user_classification_id": 0, "cpf": "", "company": "M\u00f3veis Carraro ", "role": "Assistente", "my_description": null, "matched": false, "match_id": null, "cellphone": null, "city": "Bento Gon\u00e7alves", "state": "Rio Grande do Sul", "site": null, "points": 19340.0, "avatar": "/uploads/user/avatar/8482/normal_1b505004-100c-4c51-bf49-60332ef1af5f.jpg", "avatar_thumb": "/uploads/user/avatar/8482/thumb_1b505004-100c-4c51-bf49-60332ef1af5f.jpg", "requested": false, "attribute_1": "5cf02869-2cc7-48c3-8b92-58be5af6e1fe", "attribute_2": null, "attribute_3": null, "country": null, "birth": null, "sex": null, "hash_token": "ca1ea2b9536eaf66276e80c4bd5bf64c"},
	{"id": 6698, "language": null, "allow_feed": true, "name": "Beatriz ", "email": null, "user_classification_name": null, "user_classification_id": 0, "cpf": "", "company": "\u2014\u2014", "role": "Head of Partnerships ", "my_description": "", "matched": false, "match_id": null, "cellphone": null, "city": "S\u00e3o Paulo", "state": "S\u00e3o Paulo", "site": null, "points": 4870.0, "avatar": "/uploads/user/avatar/6698/normal_671e7660-537d-4500-9d88-09d7d7503c74.jpg", "avatar_thumb": "/uploads/user/avatar/6698/thumb_671e7660-537d-4500-9d88-09d7d7503c74.jpg", "requested": false, "attribute_1": "e1605144-a328-4887-9536-754ebd912da4", "attribute_2": "", "attribute_3": "", "country": "Brasil", "birth": null, "sex": "", "hash_token": "94bce1a9df30a2474fa163ff3258c93d"},
	{"id": 364, "language": null, "allow_feed": true, "name": " A. ", "email": null, "user_classification_name": null, "user_classification_id": null, "cpf": "", "company": "Empatia MKT", "role": "Diretoria (C-Level)", "my_description": null, "matched": false, "match_id": null, "cellphone": null, "city": "Sapiranga", "state": "Rio Grande do Sul", "site": null, "points": 3150.0, "avatar": "/images/user.jpg", "avatar_thumb": "/images/user.jpg", "requested": false, "attribute_1": "d7954485-6cdb-4294-ad9d-27a8ec315627", "attribute_2": null, "attribute_3": null, "country": null, "birth": null, "sex": null, "hash_token": "ade2cce26489cc8dddc64734bb5ab283"}
]
$$) AS x (
	"id" bigint,
	"language" TEXT,
	"allow_feed" BOOL,
	"name" TEXT,
	"email" TEXT,
	"user_classification_name" TEXT,
	"user_classification_id" TEXT,
	"cpf" text,
	"company" text,
	"role" text,
	"my_description" TEXT,
	"matched" BOOLEAN,
	"match_id" TEXT,
	"cellphone" TEXT,
	"city" TEXT,
	"state" TEXT,
	"site" TEXT,
	"points" REAL,
	"avatar" text,
	"avatar_thumb" text,
	"requested" boolean,
	"attribute_1" text,
	"attribute_2" text,
	"attribute_3" text,
	"country" text,
	"birth" text,
	"sex" text,
	"hash_token" text);
