///////////////domain///////////////q

//domain/user.ts
interface UserDto {
  name: string;
}

//domain/userrepo.ts
interface UserRepo {
  create: (user: UserDto) => User;
}

//domain/user.ts
interface User extends UserDto {
  id: number;
}

///////////////application//////////////

//application/create_user.ts
function create_user(user: UserDto, repository: UserRepo) {
  //logica
  return repository.create(user);
}

////////////////infraestructure///////////////////

//infraestructure/user_repo.ts
class UserRepoImpl implements UserRepo {
  pool: any;
  constructor(pool: any) {
    this.pool = pool;
  }
  create = (user: UserDto) => {
    this.pool.save(user);
    return {
      id: 1,
      name: user.name
    };
  };
}

/////////////////////////main.py//////////////////

//index.ts
function init() {
  const user: UserDto = {
    name: 'Rafael'
  };
  const pool = {
    save: (user: UserDto) => user
  };
  const userRepositoryImple = new UserRepoImpl(pool);

  create_user(user, userRepositoryImple);
}

init();
